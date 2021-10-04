import datetime as dt
from library.ftx.base import AsyncBaseApiClass


class Markets(AsyncBaseApiClass):
    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name)

    async def get_markets(self):
        """ https://docs.ftx.com/#markets """
        return await self.get('/api/markets', authentication_required=False)

    async def get_single_market(self, market_name: str):
        """ https://docs.ftx.com/#get-single-market """
        return await self.get(f'/api/markets/{market_name}', authentication_required=False)

    async def get_orderbook(self, market_name: str, depth: float):
        """ https://docs.ftx.com/#get-orderbook """
        return await self.get(f'/api/markets/{market_name}/orderbook?depth={depth}', authentication_required=False)

    async def get_trades(self, market_name: str, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-trades """
        return await self.get(f'/api/markets/{market_name}/trades', authentication_required=False, start_time=start_time, end_time=end_time)

    async def get_historical_prices(self, market_name: str, resolution: int, start_time: dt.datetime, end_time: dt.datetime):
        """ https://docs.ftx.com/#get-historical-index """
        start_ts, end_ts = start_time.timestamp(), end_time.timestamp()
        return await self.get(f'/api/markets/{market_name}/candles?resolution={resolution}&start_time={start_ts}&end_time={end_ts}')
