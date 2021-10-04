from library.ftx.base import AsyncBaseApiClass


class LatencyStatistics(AsyncBaseApiClass):
    """docstring for Fills."""

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name)

    async def get(self, days: int = None, subaccount_nickname: str = None):
        """ https://docs.ftx.com/#latency-statistics """
        return self.get('/api/stats/latency_stats', days=days, subaccount_nickname=subaccount_nickname)
