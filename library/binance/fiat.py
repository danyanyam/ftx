from base import BaseApiClass
import datetime as dt

# TODO Enums, Raises


class Fiat(BaseApiClass):
    """https://binance-docs.github.io/apidocs/spot/en/#fiat-endpoints"""

    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)

    def get_fiat_deposit_withdraw_history(self,
                                          transactionType: str = None,
                                          beginTime: dt.datetime = None,
                                          endTime: dt.datetime = None,
                                          page: int = None,
                                          rows: int = None,
                                          recvWindow: int = None,
                                          time_req: bool = True,
                                          sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-fiat-deposit-withdraw-history-user_data"""
        return self.get('/sapi/v1/fiat/orders',
                        transactionType=transactionType,
                        beginTime=beginTime,
                        endTime=endTime,
                        page=page,
                        rows=rows,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_fiat_payments_history(self,
                                  transactionType: str = None,
                                  beginTime: dt.datetime = None,
                                  endTime: dt.datetime = None,
                                  page: int = None,
                                  rows: int = None,
                                  recvWindow: int = None,
                                  time_req: bool = True,
                                  sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-fiat-payments-history-user_data"""
        return self.get('/sapi/v1/fiat/payments',
                        transactionType=transactionType,
                        beginTime=beginTime,
                        endTime=endTime,
                        page=page,
                        rows=rows,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)
