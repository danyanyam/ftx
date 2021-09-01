from base import BaseApiClass


class Wallet(BaseApiClass):
    """https://binance-docs.github.io/apidocs/spot/en/#wallet-endpoints"""

    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)
