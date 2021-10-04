
import datetime as dt
from library.ftx.base import AsyncBaseApiClass


class FundingPayments(AsyncBaseApiClass):
    """docstring for FundingPayments."""

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name)

    async def get(self, future: str = '', start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#funding-payments """
        return await self.get('/api/funding_payments', future=future, start_time=start_time, end_time=end_time)