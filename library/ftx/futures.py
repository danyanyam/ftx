import datetime as dt

from library.ftx.base import ApiObject

# TODO: historical index


class Futures(ApiObject):
    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name)

    async def list_all_futures(self):
        """ https://docs.ftx.com/#futures """
        return await self.get('/futures', authentication_required=False)

    async def get_future(self, future_name: str):
        """ https://docs.ftx.com/#get_future """
        return await self.get(f'/futures/{future_name}', authentication_required=False)

    async def get_future_stats(self, future_name: str):
        """ https://docs.ftx.com/#get_future """
        return await self.get(f'/futures/{future_name}/stats', authentication_required=False)

    async def get_funding_rates(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-funding-rates """
        return await self.get(f'/funding_rates', authentication_required=False, start_time=start_time, end_time=end_time)

    async def get_index_weights(self, index_name: str):
        """ https://docs.ftx.com/#get-index-weights """
        return await self.get(f'/indexes/{index_name}/weights', authentication_required=False)

    async def get_expired_futures(self):
        """ https://docs.ftx.com/#get-index-weights """
        return await self.get(f'/expired_futures', authentication_required=False)
