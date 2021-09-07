from base import BaseApiClass
import datetime as dt

# TODO Enums, Raises


class Margin(BaseApiClass):
    """https://binance-docs.github.io/apidocs/spot/en/#margin-account-trade"""

    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)

    def cross_margin_account_transfer(self,
                                      asset: str = 'BTC',
                                      amount: float = 0.01,
                                      type: int = 1,
                                      recvWindow: int = None,
                                      time_req: bool = True,
                                      sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#cross-margin-account-transfer-margin"""
        return self.post('/sapi/v1/margin/transfer',
                         asset=asset,
                         amount=amount,
                         type=type,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def margin_account_borrow(self,
                              asset: str = 'BTC',
                              isIsolated: str = None,
                              symbol: str = None,
                              amount: float = 0.00001,
                              recvWindow: int = None,
                              time_req: bool = True,
                              sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#margin-account-borrow-margin"""
        return self.post('/sapi/v1/margin/loan',
                         asset=asset,
                         isIsolated=isIsolated,
                         symbol=symbol,
                         amount=amount,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)
