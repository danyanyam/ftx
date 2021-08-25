from library.ftx.base import ApiObject

class Account(ApiObject):
    """https://docs.ftx.com/#account"""

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = None):
        super().__init__(api_key, secret_key, subaccount_name)

    async def get_account_information(self):
        """ https://docs.ftx.com/#get-account-information """
        return await self.get('/api/account')

    async def get_positions(self):
        """ https://docs.ftx.com/#get-positions """
        return await self.get('/api/positions')

    async def change_account_leverage(self, leverage: float):
        """ https://docs.ftx.com/#change-account-leverage """
        assert leverage < 2
        return await self.post('/api/account/leverage', data={'leverage': leverage})

