from library.ftx.base import BaseApiClass


class Staking(BaseApiClass):

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name)

    def get_stakes(self):
        """ https://docs.ftx.com/#staking """
        return self.get('/api/staking/stakes')

    def unstake_request(self):
        """ https://docs.ftx.com/#unstake-request """
        return self.get('/api/staking/unstake_request')

    def unstake_request_(self, coin: str, size: float):
        """ https://docs.ftx.com/#unstake-request-2 """
        return self.post('/api/staking/unstake_request', data={'coin': coin, 'size': size})

    def get_stake_balance(self):
        """ https://docs.ftx.com/#get-stake-balances """
        return self.get('/api/staking/balances')

    def cancel_unstake_request(self,  request_id: int):
        """ https://docs.ftx.com/#cancel-unstake-request """
        return self.delete(f'/api/staking/unstake_requests/{request_id}')

    def get_staking_rewards(self):
        """ https://docs.ftx.com/#get-staking-rewards """
        return self.delete(f'/api/staking/staking_rewards')

    def stake_request(self, coin: str, size: float):
        """ https://docs.ftx.com/#stake-request """
        return self.post('/api/srm_stakes/stakes', data={'coin': coin, 'size': size})
