from library.ftx.base import ApiObject

class Account(ApiObject):
    """https://docs.ftx.com/#account"""

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = None):
        super().__init__(api_key, secret_key, subaccount_name)

    async def get_account_information(self):
        return await self.get('/api/account')

    async def get_positions(self):
        return await self.get('/api/positions')

