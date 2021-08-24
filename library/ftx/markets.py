from library.utils import _get

# TODO: get historical prices

class Markets:
    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key

    async def get_markets(self):
        """ https://docs.ftx.com/#markets """
        return await self.get('/markets', authentication_requires=False)

    async def get_single_market(self, market_name: str):
        """ https://docs.ftx.com/#get-single-market """
        return await self.get(f'/markets/{market_name}', authentication_requires=False)

    async def get_orderbook(self, market_name: str, depth: float):
        """ https://docs.ftx.com/#get-orderbook """
        return await self.get(f'/markets/{market_name}/orderbook?depth={depth}', authentication_requires=False)

    async def get_trades(self, market_name: str):
        """ https://docs.ftx.com/#get-trades """
        return await self.get(f'/markets/{market_name}/trades', authentication_requires=False)

    async def get(self, endpoint: str, authentication_requires: bool = True):
        return await _get(endpoint, is_auth=authentication_requires, api_key=self.api_key, secret_key=self.secret_key)
