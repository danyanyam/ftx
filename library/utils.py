import aiohttp
import time
import hmac
import json

from typing import Any, Dict

API = 'https://ftx.com'


async def get(url: str, authenticated: bool = False, api_key: str = '', secret_key: str = '') -> Dict:
    """ basic get request, using async """

    headers = build_header(method='GET', endpoint=url, api_key=api_key, secret_key=secret_key) if authenticated else None
    async with aiohttp.ClientSession() as request:
        async with request.get(API + url, headers=headers) as response:
            return await response.json()


async def post(url: str, data: Dict[str, Any], headers: Dict[str, str] = None,  authenticated: bool = False, api_key: str = '', secret_key: str = '') -> Dict:
    """ basic post request, using async """

    headers = build_header(method='POST', endpoint=url, api_key=api_key, secret_key=secret_key, data=data) if authenticated else None
    async with aiohttp.ClientSession(headers=headers) as request:
        async with request.post(API + url, data=data) as response:
            return await response.json()


def build_header(method: str, endpoint: str, api_key: str, secret_key: str, subaccount_name: str = '', data: Dict[str, str] = None):
    assert method in ('POST', 'GET')

    ts = int(time.time() * 1000)
    data = json.dumps(data) if data else ''
    signature_payload = f'{ts}{method}{endpoint}{data}'.encode()
    signature = hmac.new(secret_key.encode(), signature_payload, 'sha256').hexdigest()
    headers = {'FTX-KEY': api_key, 'FTX-SIGN': signature, 'FTX-TS': str(ts)}

    if subaccount_name:
        headers.update({'FTX-SUBACCOUNT': subaccount_name})

    return headers
