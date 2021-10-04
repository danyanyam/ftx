from base import BaseApiClass
import datetime as dt

# TODO Enums, Raises


class C2C(BaseApiClass):
    """https://binance-docs.github.io/apidocs/spot/en/#c2c-endpoints"""

    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)

    def get_fiat_deposit_withdraw_history(self,
                                          tradeType: str = None,
                                          startTimestamp: dt.datetime = None,
                                          endTimestamp: dt.datetime = None,
                                          page: int = None,
                                          rows: int = None,
                                          recvWindow: int = None,
                                          time_req: bool = True,
                                          sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-c2c-trade-history-user_data"""
        return self.get('/sapi/v1/c2c/orderMatch/listUserOrderHistory',
                        transactionType=tradeType,
                        beginTime=startTimestamp,
                        endTimestamp=endTimestamp,
                        page=page,
                        rows=rows,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)
