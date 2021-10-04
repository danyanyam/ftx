from base import BaseApiClass
import datetime as dt

# TODO Enums, Raises


class BSSwap(BaseApiClass):
    """https://binance-docs.github.io/apidocs/spot/en/#margin-account-trade"""

    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)

    def list_all_swap_pools(self,
                            recvWindow: int = None,
                            time_req: bool = True,
                            sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#blvt-nav-kline-candlestick-streams"""
        return self.get('/sapi/v1/bswap/pools')

    def get_liquidity_information_of_a_pool(self,
                                            poolId: str = None,
                                            recvWindow: int = None,
                                            time_req: bool = True,
                                            sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-liquidity-information-of-a-pool-user_data"""
        return self.get('/sapi/v1/bswap/liquidity',
                        poolId=poolId,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def add_liquidity(self,
                      poolId: str = None,
                      asset: str = None,
                      quantity: float = None,
                      recvWindow: int = None,
                      time_req: bool = True,
                      sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#add-liquidity-trade"""
        return self.post('/sapi/v1/bswap/liquidityAdd',
                         poolId=poolId,
                         asset=asset,
                         quantity=quantity,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def remove_liquidity(self,
                         poolId: str = None,
                         type: str = None,
                         asset: str = None,
                         shareAmount: float = None,
                         recvWindow: int = None,
                         time_req: bool = True,
                         sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#remove-liquidity-trade"""
        return self.post('/sapi/v1/bswap/liquidityRemove',
                         poolId=poolId,
                         type=type,
                         asset=asset,
                         shareAmount=shareAmount,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def get_liquidity_operation_record(self,
                                       operationId: str = None,
                                       poolId: str = None,
                                       operation: str = None,
                                       start_time: dt.datetime = None,
                                       end_time: dt.datetime = None,
                                       limit: int = None,
                                       recvWindow: int = None,
                                       time_req: bool = True,
                                       sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-liquidity-operation-record-user_data"""
        return self.get('/sapi/v1/bswap/liquidityOps',
                        operationId=operationId,
                        poolId=poolId,
                        operation=operation,
                        start_time=start_time,
                        end_time=end_time,
                        limit=limit,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def request_quote(self,
                      quoteAsset: str = None,
                      baseAsset: str = None,
                      quoteQty: float = None,
                      recvWindow: int = None,
                      time_req: bool = True,
                      sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#request-quote-user_data"""
        return self.get('/sapi/v1/bswap/quote',
                        quoteAsset=quoteAsset,
                        baseAsset=baseAsset,
                        quoteQty=quoteQty,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def swap(self,
             quoteAsset: str = None,
             baseAsset: str = None,
             quoteQty: float = None,
             recvWindow: int = None,
             time_req: bool = True,
             sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#swap-trade"""
        return self.post('/sapi/v1/bswap/swap',
                         quoteAsset=quoteAsset,
                         baseAsset=baseAsset,
                         quoteQty=quoteQty,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    def get_swap_history(self,
                         swapId: int = None,
                         start_time: dt.datetime = None,
                         end_time: dt.datetime = None,
                         status: int = None,
                         quoteAsset: str = None,
                         baseAsset: str = None,
                         limit: int = None,
                         recvWindow: int = None,
                         time_req: bool = True,
                         sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#get-swap-history-user_data"""
        return self.get('/sapi/v1/bswap/swap',
                        swapId=swapId,
                        start_time=start_time,
                        end_time=end_time,
                        status=status,
                        baseAsset=baseAsset,
                        quoteAsset=quoteAsset,
                        limit=limit,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)
