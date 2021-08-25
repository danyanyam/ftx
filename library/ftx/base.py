import datetime as dt
import aiohttp
import time
import hmac
import json
from typing import Dict

API = 'https://ftx.com'


def both_args_present_or_not(lhs=None, rhs=None):
    """ function is used to determine, that both arguments
    are either passsed or excluded """
    return all([lhs, rhs]) or not any([lhs, rhs])


class ApiObject:
    def __init__(self, api_key: str, secret_key: str, subaccount_name: str):
        self.api_key = api_key
        self.secret_key = secret_key
        self.subaccount_name = subaccount_name

    async def get(self, endpoint: str, authentication_required: bool = True, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ Basic get request """
        assert both_args_present_or_not(start_time, end_time), f'choose either both start_time & end_time, or nothing'

        # pagination support
        params = {'start_time': start_time, 'end_time': end_time} if all([start_time, end_time]) else {}
        headers = await self._build_header(method='GET', endpoint=endpoint) if authentication_required else None

        async with aiohttp.ClientSession(headers=headers) as request:
            async with request.get(API + endpoint, params=params) as response:
                return await response.json()

    async def post(self, endpoint: str, data: Dict[str, str], authentication_required: bool = True, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ Basic post request """
        assert both_args_present_or_not(start_time, end_time), f'choose either both start_time & end_time, or nothing'

        # pagination support
        params = {'start_time': start_time, 'end_time': end_time} if all([start_time, end_time]) else {}
        headers = await self._build_header(method='POST', endpoint=endpoint, data=data) if authentication_required else None

        async with aiohttp.ClientSession(headers=headers) as request:
            async with request.post(API + endpoint, data=data, params=params) as response:
                return await response.json()

    async def _build_header(self, method: str, endpoint: str, data: Dict[str, str] = None):
        """ in order to do some actions (like withdrawals) authentication is required.
        this functions builds headers, which are sento together with requests"""

        assert method in ('POST', 'GET')

        ts = int(time.time() * 1000)
        data = json.dumps(data) if data else ''
        signature_payload = f'{ts}{method}{endpoint}{data}'.encode()
        signature = hmac.new(self.secret_key.encode(), signature_payload, 'sha256').hexdigest()
        headers = {'FTX-KEY': self.api_key, 'FTX-SIGN': signature, 'FTX-TS': str(ts)}

        if self.subaccount_name:
            headers.update({'FTX-SUBACCOUNT': self.subaccount_name})

        return headers
