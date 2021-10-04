from library.ftx.base import BaseApiClass

class Subaccounts(BaseApiClass):

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name)

    def get_all_subaccounts(self):
        """ https://docs.ftx.com/#get-all-subaccounts """
        return self.get('/api/subaccounts')

    def get_subaccount_balances(self, nickname: str):
        """ https://docs.ftx.com/#get-all-subaccounts """
        return self.get(f'/api/subaccounts/{nickname}/balances')

    def create_subaccounts(self, nickname: str):
        """ https://docs.ftx.com/#create-subaccount """
        return self.post('/api/subaccounts', data={'nickname': nickname})

    def change_subaccount_name(self, nickname: str, newNickname: str):
        """ https://docs.ftx.com/#change-subaccount-name """
        return self.post('/api/subaccounts/update_name', data={'nickname': nickname, 'newNickname': newNickname})

    def transfer_between_subaccounts(self, coin: str, size: float, source: str, destination: str):
        """ https://docs.ftx.com/#transfer-between-subaccounts """
        return self.post('/api/subaccounts/transfer', data={'coin': coin, 'size': size, 'source': source, 'destination': destination})

    def delete_subaccount(self, nickname: str):
        """ https://docs.ftx.com/#delete-subaccount """
        return self.delete('/api/subaccounts', data={'nickname': nickname})