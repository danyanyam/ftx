import datetime as dt
import aiohttp
import time
import hmac
import json
from typing import Dict
import urllib

API = 'https://api.binance.com'


class BaseApiClass:
    def __init__(self, api_key: str, secret_key: str, api=API):
        self.api_key = api_key
        self.secret_key = secret_key
        self.api = api

    def get(self, endpoint: str, headers = {}):
        with aiohttp.ClientSession(headers=headers) as request:
            with request.get(self.api + endpoint) as response:
                return response.json()
    # async def get(self, endpoint: str, authentication_required: bool = True, start_time: dt.datetime = None, end_time: dt.datetime = None, **kwargs):
    #     """ Basic get request """
    #     assert both_args_present_or_not(start_time, end_time), f'choose either both start_time & end_time, or nothing'

    #     # pagination support
    #     params = {'start_time': start_time, 'end_time': end_time} if all([start_time, end_time]) else {}
    #     params.update(delete_keys_with_empty_values(kwargs))

    #     endpoint = create_endpoint_from_arguments(endpoint, params)
    #     headers =  self._build_header(method='GET', endpoint=endpoint) if authentication_required else None

    #     with aiohttp.ClientSession(headers=headers) as request:
    #         with request.get(self.api + endpoint) as response:
    #             return response.json()