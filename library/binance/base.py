import requests
import hmac
import hashlib
import json
import aiohttp
from urllib.parse import urlencode

API = 'https://api.binance.com'

# TO DO: Security Type refactoring


def server_time():
    """Make a request to the API to get server time

    Returns:
        server_time: int
    """
    servertime = requests.get("https://api.binance.com/api/v1/time")
    servertimeobject = json.loads(servertime.text)
    server_time = servertimeobject['serverTime']
    return server_time


class BaseApiClass:
    def __init__(self, api_key: str, secret_key: str, api=API):
        self.api_key = api_key
        self.secret_key = secret_key
        self.api = api

    def _build_params(self, sign: bool, time_req: bool, params):
        params = {k: v for k, v in params.items() if v is not None}
        params.update({'timestamp': server_time()}) if time_req else None

        params_sign = params
        if sign:
            params_sign = urlencode(params_sign)
            signature = hmac.new(self.secret_key.encode(), params_sign.encode(), hashlib.sha256).hexdigest()
            params.update({'signature': signature})

        return params

    def _build_headers(self):
        headers = {"X-MBX-APIKEY": self.api_key}
        return headers

    async def get(self,
                  endpoint: str,
                  sign: bool = False,
                  time_req: bool = False,
                  authentication_required: bool = True,
                  **kwargs):

        params = self._build_params(sign, time_req, params=kwargs)
        headers = self._build_headers() if authentication_required else None

        async with aiohttp.ClientSession(headers=headers) as request:
            async with request.get(self.api + endpoint, params=params, ssl=False) as response:
                return await response.json()

    async def post(self,
                   endpoint: str,
                   sign: bool = False,
                   time_req: bool = False,
                   authentication_required: bool = True,
                   **kwargs):

        params = self._build_params(sign, time_req, params=kwargs)
        headers = self._build_headers() if authentication_required else None

        async with aiohttp.ClientSession(headers=headers) as request:
            async with request.post(self.api + endpoint, params=params, ssl=False) as response:
                return await response.json()

    async def delete(self,
                     endpoint: str,
                     sign: bool = False,
                     time_req: bool = False,
                     authentication_required: bool = True,
                     **kwargs):

        params = self._build_params(sign, time_req, params=kwargs)
        headers = self._build_headers() if authentication_required else None

        async with aiohttp.ClientSession(headers=headers) as request:
            async with request.post(self.api + endpoint, params=params, ssl=False) as response:
                return await response.json()
