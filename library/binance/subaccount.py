from base import BaseApiClass


class Subaccount(BaseApiClass):
    """https://binance-docs.github.io/apidocs/spot/en/#sub-account-endpoints"""

    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)

    def create_virtial_subaccount(self,
                                  subAccountString: str = 'API_test',
                                  recvWindow: int = None,
                                  time_req: bool = True,
                                  sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#create-a-virtual-sub-account-for-master-account"""
        return self.post('/sapi/v1/sub-account/virtualSubAccount',
                         subAccountString=subAccountString, recvWindow=recvWindow, time_req=time_req, sign=sign)

    # Output:{'code': 200001054}.
    # After careful reading of documentation, it can be seen, that Subaccount End-Point are only for Corporate Accounts
