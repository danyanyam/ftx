from base import BaseApiClass
import datetime as dt

# TODO Enums, Raises


class BLVT(BaseApiClass):
    """https://binance-docs.github.io/apidocs/spot/en/#blvt-endpoints"""

    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)

    def get_BLVT_info(self,
                      tokenName: str = None,
                      recvWindow: int = None,
                      time_req: bool = True,
                      sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#cross-margin-account-transfer-margin"""
        return self.get('/sapi/v1/blvt/tokenInfo',
                        tokenName=tokenName,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def subscribe_BLVT(self,
                       tokenName: str = None,
                       cost: float = None,
                       recvWindow: int = None,
                       time_req: bool = True,
                       sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#subscribe-blvt-user_data"""
        return self.post('/sapi/v1/blvt/subscribe',
                         tokenName=tokenName,
                         cost=cost,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def query_subscription_record(self,
                                  tokenName: str = None,
                                  id: int = None,
                                  start_time: dt.datetime = None,
                                  end_time: dt.datetime = None,
                                  limit: int = None,
                                  recvWindow: int = None,
                                  time_req: bool = True,
                                  sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-subscription-record-user_data"""
        return self.get('/sapi/v1/blvt/subscribe/record',
                        tokenName=tokenName,
                        id=id,
                        start_time=start_time,
                        end_time=end_time,
                        limit=limit,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def redeem_BLVT(self,
                    tokenName: str = None,
                    amount: float = None,
                    recvWindow: int = None,
                    time_req: bool = True,
                    sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#redeem-blvt-user_data"""
        return self.post('/sapi/v1/blvt/redeem',
                         tokenName=tokenName,
                         amount=amount,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def query_redemption_record(self,
                                tokenName: str = None,
                                id: int = None,
                                start_time: dt.datetime = None,
                                end_time: dt.datetime = None,
                                limit: int = None,
                                recvWindow: int = None,
                                time_req: bool = True,
                                sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-redemption-record-user_data"""
        return self.get('/sapi/v1/blvt/redeem/record',
                        tokenName=tokenName,
                        id=id,
                        start_time=start_time,
                        end_time=end_time,
                        limit=limit,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def get_BLVT_user_limit_info(self,
                                 tokenName: str = None,
                                 recvWindow: int = None,
                                 time_req: bool = True,
                                 sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-blvt-user-limit-info-user_data"""
        return self.get('/sapi/v1/blvt/userLimit',
                        tokenName=tokenName,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)
