from library.ftx.base import AsyncBaseApiClass


class Staking(AsyncBaseApiClass):

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name)

    async def get_stakes(self):
        """ https://docs.ftx.com/#staking """
        return await self.get('/api/staking/stakes')

    async def unstake_request(self):
        """ https://docs.ftx.com/#unstake-request """
        return await self.get('/api/staking/unstake_request')

    async def unstake_request_(self, coin: str, size: float):
        """ https://docs.ftx.com/#unstake-request-2 """
        return await self.post('/api/staking/unstake_request', data={'coin': coin, 'size': size})

    async def get_stake_balance(self):
        """ https://docs.ftx.com/#get-stake-balances """
        return await self.get('/api/staking/balances')

    async def cancel_unstake_request(self,  request_id: int):
        """ https://docs.ftx.com/#cancel-unstake-request """
        return await self.delete(f'/api/staking/unstake_requests/{request_id}')

    async def get_staking_rewards(self):
        """ https://docs.ftx.com/#get-staking-rewards """
        return await self.delete(f'/api/staking/staking_rewards')

    async def stake_request(self, coin: str, size: float):
        """ https://docs.ftx.com/#stake-request """
        return await self.post('/api/srm_stakes/stakes', data={'coin': coin, 'size': size})
