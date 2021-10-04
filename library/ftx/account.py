from library.ftx.base import BaseApiClass

class Account(BaseApiClass):
    """https://docs.ftx.com/#account"""

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = None):
        super().__init__(api_key, secret_key, subaccount_name)

    def get_account_information(self):
        """ https://docs.ftx.com/#get-account-information """
        return self.get('/api/account')

    def get_positions(self):
        """ https://docs.ftx.com/#get-positions """
        return self.get('/api/positions')

    def change_account_leverage(self, leverage: float):
        """ https://docs.ftx.com/#change-account-leverage """
        assert leverage < 2
        return self.post('/api/account/leverage', data={'leverage': leverage})


