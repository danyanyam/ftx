import datetime as dt
from library.ftx.base import AsyncBaseApiClass


class Fills(AsyncBaseApiClass):
    """docstring for Fills."""

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name)

    async def get(self, market: str = '', start_time: dt.datetime = None, end_time: dt.datetime = None, order: str = '', orderId: str = ''):
        """ https://docs.ftx.com/#fills """
        return self.get('/api/fills', market=market, start_time=start_time, end_time=end_time, order=order, orderId=orderId)
