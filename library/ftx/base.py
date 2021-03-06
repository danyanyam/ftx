import time
import hmac
import json
import urllib
import aiohttp
import requests
import datetime as dt
from typing import Dict

from library.logging import Logger

logger = Logger('FTX', console_level='ERROR').get_logger()
API = 'https://ftx.com'


def create_endpoint_from_arguments(endpoint: str, args: Dict[str, str]):
    result = urllib.parse.urlencode(args)
    if result:
        result = '?' + result
    return endpoint + result


def delete_keys_with_empty_values(d: Dict[str, str]):
    return {key: value for key, value in d.items() if value}


def both_args_present_or_not(lhs=None, rhs=None):
    """ function is used to determine, that both arguments
    are either passsed or excluded """
    return all([lhs, rhs]) or not any([lhs, rhs])


class AsyncBaseApiClass:
    def __init__(self, api_key: str, secret_key: str, subaccount_name: str, api=API):
        self.api_key = api_key
        self.secret_key = secret_key
        self.subaccount_name = subaccount_name
        self.api = api

    async def get(self, endpoint: str, authentication_required: bool = True, start_time: dt.datetime = None, end_time: dt.datetime = None, **kwargs):
        """ Basic get request """
        assert both_args_present_or_not(start_time, end_time), f'choose either both start_time & end_time, or nothing'

        # pagination support
        params = {'start_time': start_time, 'end_time': end_time} if all([start_time, end_time]) else {}
        params.update(delete_keys_with_empty_values(kwargs))

        endpoint = create_endpoint_from_arguments(endpoint, params)
        headers = await self._build_header(method='GET', endpoint=endpoint) if authentication_required else None

        async with aiohttp.ClientSession(headers=headers) as request:
            async with request.get(self.api + endpoint) as response:
                response = await response.json()
                self.check_response(response)
                return response

    async def post(self, endpoint: str, data: Dict[str, str], authentication_required: bool = True, start_time: dt.datetime = None, end_time: dt.datetime = None, **kwargs):
        """ Basic post request """
        assert both_args_present_or_not(start_time, end_time), f'choose either both start_time & end_time, or nothing'

        # pagination support
        params = {'start_time': start_time, 'end_time': end_time} if all([start_time, end_time]) else {}
        params.update(delete_keys_with_empty_values(kwargs))

        headers = await self._build_header(method='POST', endpoint=endpoint, data=data) if authentication_required else None

        async with aiohttp.ClientSession(headers=headers) as request:
            async with request.post(self.api + endpoint, data=data, params=params) as response:
                response = await response.json()
                self.check_response(response)
                return response

    async def delete(self, endpoint: str, data: Dict[str, str], authentication_required: bool = True):
        """ Basic delete request """

        data = delete_keys_with_empty_values(data)
        headers = await self._build_header(method='DELETE', endpoint=endpoint, data=data) if authentication_required else None
        async with aiohttp.ClientSession(headers=headers) as request:
            async with request.delete(self.api + endpoint, data=data) as response:
                response = await response.json()
                self.check_response(response)
                return response

    async def _build_header(self, method: str, endpoint: str, data: Dict[str, str] = None):
        """ in order to do some actions (like withdrawals) authentication is required.
        this functions builds headers, which are sento together with requests"""

        assert method in ('POST', 'GET')

        ts = int(time.time() * 1000)
        data = json.dumps(data).encode() if data else ''
        signature_payload = f'{ts}{method}{endpoint}{data}'.encode()
        signature = hmac.new(self.secret_key.encode(), signature_payload, 'sha256').hexdigest()
        headers = {'FTX-KEY': self.api_key, 'FTX-SIGN': signature, 'FTX-TS': str(ts)}

        if self.subaccount_name:

            headers.update({'FTX-SUBACCOUNT': urllib.parse.quote(self.subaccount_name)})

        return headers

    def check_response(self, response):
        if not response['success']:
            logger.error(f'API fetch failed. Reason: {response["error"]}')


class BaseApiClass:
    def __init__(self, api_key: str, secret_key: str, subaccount_name: str, api=API):
        self.api_key = api_key
        self.secret_key = secret_key
        self.subaccount_name = subaccount_name
        self.api = api

    def get(self, endpoint: str, authentication_required: bool = True, start_time: dt.datetime = None, end_time: dt.datetime = None, **kwargs):
        """ Basic get request """
        assert both_args_present_or_not(start_time, end_time), f'choose either both start_time & end_time, or nothing'

        # pagination support
        params = {'start_time': start_time, 'end_time': end_time} if all([start_time, end_time]) else {}
        params.update(delete_keys_with_empty_values(kwargs))

        endpoint = create_endpoint_from_arguments(endpoint, params)
        headers = self._build_header(method='GET', endpoint=endpoint) if authentication_required else None

        with requests.Session() as s:
            response = s.get(self.api + endpoint, headers=headers)
            response.raise_for_status()
            response = response.json()
            self.check_response(response)
            return response

    def post(self, endpoint: str, data: Dict[str, str], authentication_required: bool = True, start_time: dt.datetime = None, end_time: dt.datetime = None, **kwargs):
        """ Basic post request """
        assert both_args_present_or_not(start_time, end_time), f'choose either both start_time & end_time, or nothing'

        # pagination support
        params = {'start_time': start_time, 'end_time': end_time} if all([start_time, end_time]) else {}
        params.update(delete_keys_with_empty_values(kwargs))

        headers = self._build_header(method='POST', endpoint=endpoint, data=data) if authentication_required else None

        with requests.Session() as s:
            response = s.post(self.api + endpoint, data=data, params=params)
            response.raise_for_status()
            response = response.json()
            self.check_response(response)
            return response

    async def delete(self, endpoint: str, data: Dict[str, str], authentication_required: bool = True):
        """ Basic delete request """

        data = delete_keys_with_empty_values(data)
        headers = self._build_header(method='DELETE', endpoint=endpoint, data=data) if authentication_required else None
        with requests.Session() as s:
            response = s.delete(self.api + endpoint, data=data, headers=headers)
            response.raise_for_status()
            response = response.json()
            self.check_response(response)
            return response

    def _build_header(self, method: str, endpoint: str, data: Dict[str, str] = None):
        """ in order to do some actions (like withdrawals) authentication is required.
        this functions builds headers, which are sento together with requests"""

        assert method in ('POST', 'GET')

        ts = int(time.time() * 1000)
        data = json.dumps(data).encode() if data else ''
        signature_payload = f'{ts}{method}{endpoint}{data}'.encode()
        signature = hmac.new(self.secret_key.encode(), signature_payload, 'sha256').hexdigest()
        headers = {'FTX-KEY': self.api_key, 'FTX-SIGN': signature, 'FTX-TS': str(ts)}

        if self.subaccount_name:

            headers.update({'FTX-SUBACCOUNT': urllib.parse.quote(self.subaccount_name)})

        return headers

    def check_response(self, response):
        if not response['success']:
            logger.error(f'API fetch failed. Reason: {response["error"]}')
