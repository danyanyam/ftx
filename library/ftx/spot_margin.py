import datetime as dt
from library.ftx.base import BaseApiClass


class SpotMatgin(BaseApiClass):

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name)

    async def get_lending_history(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-lending-history """
        return await self.get('/api/spot_margin/history', start_time=start_time, end_time=end_time)

    async def get_borrow_rates(self):
        """ https://docs.ftx.com/#get-borrow-rates """
        return await self.get('/api/spot_margin/borrow_rates')

    async def get_lending_rates(self):
        """ https://docs.ftx.com/#get-lending-rates """
        return await self.get('/api/spot_margin/lending_rates')

    async def get_daily_borrowed_amounts(self):
        """ https://docs.ftx.com/#get-daily-borrowed-amounts """
        return await self.get('/api/spot_margin/borrow_summary')

    async def get_market_info(self, market: str):
        """ https://docs.ftx.com/#get-market-info
        Will return None if spot margin is not enabled in account settings """
        return await self.get('/api/spot_margin/market_info', market=market)

    async def get_my_borrow_history(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-my-borrow-history """
        return await self.get('/api/spot_margin/borrow_history', start_time=start_time, end_time=end_time)

    async def get_my_lending_history(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-my-lending-history """
        return await self.get('/api/spot_margin/lending_history', start_time=start_time, end_time=end_time)

    async def get_lending_offers(self):
        """ https://docs.ftx.com/#get-lending-offers """
        return await self.get('/api/spot_margin/offers')

    async def get_lending_info(self):
        """ https://docs.ftx.com/#get-lending-info """
        return await self.get('/api/spot_margin/lending_info')

    async def submit_lenfing_offer(self, coin: str, size: float, rate: float):
        """ https://docs.ftx.com/#submit-lending-offer """
        return await self.post('/api/spot_margin/lending_info', data={'coin': coin, 'size': size, 'rate': rate})