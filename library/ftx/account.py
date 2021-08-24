from typing import Any, Dict
from library.utils import get, post


class Account:
    """https://docs.ftx.com/#account"""

    def __init__(self, api: str, secret: str):
        self.api_key = api
        self.secret_key = secret

    async def get_account_information(self) -> Dict[str, Any]:
        endpoint = '/api/account'
        return await get(endpoint, authenticated=True, api_key=self.api_key, secret_key=self.secret_key)

    async def get_positions(self) -> Dict[str, Any]:
        endpoint = '/api/positions'
        return await get(endpoint, authenticated=True, api_key=self.api_key, secret_key=self.secret_key)

    async def change_account_leverage(self, leverage) -> Dict[str, Any]:
        endpoint = '/account/leverage'
        assert leverage < 10
        return await post(endpoint, authenticated=True, api_key=self.api_key, secret_key=self.secret_key, data={'leverage': leverage})
