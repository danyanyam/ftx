from library.utils import _get

# TODO: historical index


class Futures:
    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key

    async def list_all_futures(self):
        """ https://docs.ftx.com/#futures """
        return await self.get('/futures', authentication_requires=False)

    async def get_future(self, future_name: str):
        """ https://docs.ftx.com/#get_future """
        return await self.get(f'/futures/{future_name}', authentication_requires=False)

    async def get_future_stats(self, future_name: str):
        """ https://docs.ftx.com/#get_future """
        return await self.get(f'/futures/{future_name}/stats', authentication_requires=False)

    async def get_funding_rates(self):
        """ https://docs.ftx.com/#get-funding-rates """
        return await self.get(f'/funding_rates', authentication_requires=False)

    async def get_index_weights(self, index_name: str):
        """ https://docs.ftx.com/#get-index-weights """
        return await self.get(f'/indexes/{index_name}/weights', authentication_requires=False)

    async def get_expired_futures(self):
        """ https://docs.ftx.com/#get-index-weights """
        return await self.get(f'/expired_futures', authentication_requires=False)

    async def get(self, endpoint: str, authentication_requires: bool = True):
        return await _get(endpoint, is_auth=authentication_requires, api_key=self.api_key, secret_key=self.secret_key)
