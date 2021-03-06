
import datetime as dt
from library.ftx.base import BaseApiClass


class LeveragedTokens(AsyncBaseApiClass):
    """docstring for LeveragedTokens."""

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name)

    def list_leveraged_tokens(self):
        """ https://docs.ftx.com/#list-leveraged-tokens """
        return self.get('/api/lt/tokens', authentication_required=False)

    def get_token_info(self, token_name: str):
        """ https://docs.ftx.com/#get-token-info """
        return self.get(f'/api/lt/{token_name}', authentication_required=False)

    def get_leveraged_token_balances(self):
        """ https://docs.ftx.com/#get-leveraged-token-balances """
        return self.get(f'/api/lt/balances')

    def list_leveraged_token_creation_requests(self):
        """ https://docs.ftx.com/#list-leveraged-token-creation-requests """
        return self.get(f'/api/lt/creations')

    def request_leveraged_token_creation(self, token_name: str, size: float):
        """ https://docs.ftx.com/#request-leveraged-token-creation """
        return self.post(f'/api/lt/{token_name}/create', data={'size': size})

    def list_leveraged_token_redemption_requests(self):
        """ https://docs.ftx.com/#list-leveraged-token-redemption-requests """
        return self.get(f'/api/lt/redemptions')

    def request_leveraged_token_redemption(self, token_name: str, size: float):
        """ https://docs.ftx.com/#request-leveraged-token-redemption """
        return self.post(f'/api/lt/{token_name}/redeem', data={'size': size})

    def request_etf_rebalance_info(self):
        """ https://docs.ftx.com/#request-etf-rebalance-info """
        return self.get(f'/api/etfs/rebalance_info')