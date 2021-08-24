from typing import Any, Dict
from library.utils import _get, _post


class Account:
    """https://docs.ftx.com/#account"""

    def __init__(self, api: str, secret: str):
        self.api_key = api
        self.secret_key = secret

    async def get_account_information(self):
        return await self.get('/api/account')

    async def get_positions(self):
        return await self.get('/api/positions')

    async def get(self, endpoint: str, authentication_requires: bool = True):
        return await _get(endpoint, is_auth=authentication_requires, api_key=self.api_key, secret_key=self.secret_key)
