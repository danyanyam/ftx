from base import BaseApiClass
import datetime as dt

# TODO Enums, Raises
"""
https://github.com/sammchardy/python-binance/blob/master/binance/client.py
"""


class Spot(BaseApiClass):
    """https://binance-docs.github.io/apidocs/spot/en/#spot-account-trade"""

    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)

    def test_new_order(self,
                       symbol: str = 'BTCUSDT',
                       side: str = 'SELL',
                       type: str = 'LIMIT',
                       timeInForce: str = 'FOK',  # https://www.binance.com/en/support/faq/5d3fa5e5709f47e0b5f186b350da1655
                       quantity: float = 0.1,
                       quoteOrderQty: float = None,
                       price: float = 11000,
                       newClientOrderId: int = None,
                       stopPrice: float = None,
                       icebergQty: float = None,
                       newOrderRespType: str = None,
                       recvWindow: int = None,
                       time_req: bool = True,
                       sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#test-new-order-trade"""
        return self.post('/api/v3/order/test', symbol=symbol, side=side, type=type,
                         timeInForce=timeInForce, quantity=quantity, quoteOrderQty=quoteOrderQty, price=price,
                         newClientOrderId=newClientOrderId, stopPrice=stopPrice, icebergQty=icebergQty, newOrderRespType=newOrderRespType,
                         recvWindow=recvWindow, time_req=time_req, sign=sign)

    def new_order(self,
                  symbol: str = 'BTCUSDT',
                  side: str = 'SELL',
                  type: str = 'LIMIT',
                  timeInForce: str = None,
                  quantity: float = None,
                  quoteOrderQty: float = None,
                  price: float = None,
                  newClientOrderId: int = None,
                  stopPrice: float = None,
                  icebergQty: float = None,
                  newOrderRespType: str = None,
                  recvWindow: int = None,
                  time_req: bool = True,
                  sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#new-order-trade"""
        return self.post('/api/v3/order',
                         symbol=symbol,
                         side=side,
                         type=type,
                         timeInForce=timeInForce,
                         quantity=quantity,
                         quoteOrderQty=quoteOrderQty,
                         price=price,
                         newClientOrderId=newClientOrderId,
                         stopPrice=stopPrice,
                         icebergQty=icebergQty,
                         newOrderRespType=newOrderRespType,
                         recvWindow=recvWindow,
                         time_req=time_req,
                         sign=sign)

    # TODO: evaluate why cancel_order doesn't work
    def cancel_order(self,
                     symbol: str = 'BTCUSDT',
                     orderId: int = None,
                     newClientOrderId: str = None,
                     recvWindow: int = None,
                     time_req: bool = True,
                     sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#cancel-order-trade"""
        return self.delete('/api/v3/order',
                           symbol=symbol,
                           orderId=orderId,
                           newClientOrderId=newClientOrderId,
                           recvWindow=recvWindow,
                           time_req=time_req,
                           sign=sign)

    # TODO: fix error
    def cancel_all_orders(self,
                          symbol: str = 'BTCUSDT',
                          recvWindow: int = None,
                          time_req: bool = True,
                          sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#cancel-all-open-orders-on-a-symbol-trade"""
        return self.delete('api/v3/openOrders', symbol=symbol, recvWindow=recvWindow, time_req=time_req, sign=sign)

    def query_order(self,
                    symbol: str = 'BTCUSDT',
                    orderId: int = None,
                    origClientOrderId: str = None,
                    recvWindow: int = None,
                    time_req: bool = True,
                    sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#query-order-user_data"""

        if origClientOrderId is None and orderId is None:
            raise ValueError('Either orderId ot origClientOrderId must be sent')

        return self.get('/api/v3/order',
                        symbol=symbol,
                        orderId=orderId,
                        origClientOrderId=origClientOrderId,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def current_open_orders(self,
                            symbol: str = 'BTCUSDT',
                            recvWindow: int = None,
                            time_req: bool = True,
                            sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#current-open-orders-user_data"""
        return self.get('/api/v3/openOrders',
                        symbol=symbol,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)

    def all_orders(self,
                   symbol: str = 'BTCUSDT',
                   orderId: str = None,
                   start_time: dt.datetime = None,
                   end_time: dt.datetime = None,
                   limit: int = None,
                   recvWindow: int = None,
                   time_req: bool = True,
                   sign: bool = True):
        """https://binance-docs.github.io/apidocs/spot/en/#all-orders-user_data"""
        return self.get('/api/v3/allOrders',
                        symbol=symbol,
                        orderId=orderId,
                        start_time=start_time,
                        end_time=end_time,
                        limit=limit,
                        recvWindow=recvWindow,
                        time_req=time_req,
                        sign=sign)
