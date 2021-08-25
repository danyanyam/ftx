import datetime as dt
from library.ftx.base import BaseApiClass


class Orders(BaseApiClass):
    """docstring for Orders."""

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name)

    async def get_open_orders(self, market: str):
        """ https://docs.ftx.com/#get-open-orders """
        return await self.get(f'/api/orders?market={market}')

    async def get_order_history(self, market: str = '', side: str = '', orderType: str = '', start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-order-history """

        start_time = int(start_time.timestamp()) if start_time else ''
        end_time = int(end_time.timestamp()) if end_time else ''

        return await self.get(f'/api/orders/history', market=market, side=side, orderType=orderType, start_time=start_time, end_time=end_time)

    async def get_open_trigger_orders(self, market: str = '', type_: str = ''):
        """ https://docs.ftx.com/#get-open-trigger-orders """
        assert type_ in ('stop', 'trailing_stop', 'take_profit')
        return await self.get(f'/api/conditional_orders', market=market, type=type_)

    async def get_trigger_order_trigger(self, conditional_order_id: int):
        """ https://docs.ftx.com/#get-trigger-order-triggers """
        return await self.get(f'/api/conditional_orders/{conditional_order_id}/triggers')

    async def get_trigger_order_history(self, market: str = '', side: str = '', type_: str = '', orderType: str = '', start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-trigger-order-history """
        assert type_ in ('stop', 'trailing_stop', 'take_profit')
        assert orderType in ('market', 'limit')
        return await self.get(f'/api/conditional_orders/history', market=market, side=side, type_=type_, orderType=orderType, start_time=start_time, end_time=end_time)

    async def place_order(self, market: str,
                          side: str,
                          price: float,
                          type_: str,
                          size: float,
                          reduceOnly: bool = False,
                          ioc: bool = False,
                          postOnly: bool = False,
                          clientId: str = '',
                          rejectOnPriceBand: bool = False):

        """ https://docs.ftx.com/#place-order """
        assert type_ in ('limit', 'market')
        assert side in ('buy', 'sell')
        return await self.post(f'/api/orders', data={'market': market, 'side': side, 'price': price, 'type': type_, 'size': size, 'reduceOnly': reduceOnly, 'ioc': ioc, 'postOnly': postOnly, 'rejectOnPriceBand': rejectOnPriceBand, 'clientId': clientId})

    async def place_trigger_order(self, market: str,
                                  side: str,
                                  size: float,
                                  type_: str,
                                  reduceOnly: bool = False,
                                  retryUntilFilled: bool = False,
                                  triggerPrice: float = None,
                                  orderPrice: float = None,
                                  trailValue: float = None):

        """ https://docs.ftx.com/#place-order """
        assert type_ in ('stop', 'trailing_stop', 'take_profit')
        if type_ == 'stop':
            assert isinstance(triggerPrice, (float, int)), f'cant use stop loss without trigger price'
        elif type_ == 'trailing_stop':
            assert isinstance(trailValue, (float, int)), f'cant use stop loss without trigger price'
        elif type_ == 'take_profit':
            assert isinstance(triggerPrice, (float, int)), f'cant use take profit without trigger price'

        assert side in ('buy', 'sell')
        return await self.post(f'/api/conditional_orders', data={'market': market, 'side': side, 'type': type_, 'size': size, 'reduceOnly': reduceOnly, 'retryUntilFilled': retryUntilFilled, 'triggerPrice': triggerPrice, 'orderPrice': orderPrice, 'trailValue': trailValue})

    async def modify_order(self, order_id: int, price: float = None, size: float = None, clientId: str = ''):
        """ https://docs.ftx.com/#modify-order """
        assert any((price, size)), 'either price or size must be specified'
        return await self.post(f'/api/orders/{order_id}/modify', data={'price': price, 'size': size, 'clientId': clientId})

    async def modify_order_by_client_id(self, client_order_id: int,
                                        price: float = None,
                                        size: float = None,
                                        clientId: str = ''):
        """ https://docs.ftx.com/#modify-order-by-client-id """
        assert any((price, size)), 'either price or size must be specified'
        return await self.post(f'/api/orders/by_client_id/{client_order_id}/modify', data={'price': price, 'size': size, 'clientId': clientId})

    async def modify_trigger_order(self, order_id: int,
                                   triggerPrice: float = None,
                                   orderPrice: float = None,
                                   trailValue: float = None,
                                   size: float = None):
        """ https://docs.ftx.com/#modify-trigger-order """
        return await self.post(f'/api/conditional_orders/{order_id}/modify', data={'triggerPrice': triggerPrice, 'orderPrice': orderPrice, 'trailValue': trailValue, 'size': size})

    async def get_order_status(self, order_id: int):
        """ https://docs.ftx.com/#get-order-status """
        return await self.get(f'/api/orders/{order_id}')

    async def get_order_status_by_client_id(self, client_order_id: int):
        """ https://docs.ftx.com/#get-order-status-by-client-id """
        return await self.get(f'/api/orders/by_client_id/{client_order_id}')

    async def cancel_order(self, order_id: int):
        """ https://docs.ftx.com/#cancel-order """
        return await self.delete(f'/api/orders/{order_id}')

    async def cancel_order_by_client_id(self, client_order_id: int):
        """ https://docs.ftx.com/#cancel-order-by-client-id """
        return await self.delete(f'/api/orders/by_client_id/{client_order_id}')

    async def cancel_open_trigger_order(self, id: int):
        """ https://docs.ftx.com/#cancel-open-trigger-order """
        return await self.delete(f'/api/conditional_orders/{id}')

    async def cancel_all_orders(self, market: str = '', side: str = '', conditionalOrdersOnly: bool = False, limitOrdersOnly: bool = False):
        """ https://docs.ftx.com/#cancel-all-orders """
        return await self.delete(f'/api/orders', data={'market': market, 'side': side, 'conditionalOrdersOnly': conditionalOrdersOnly, 'limitOrdersOnly': limitOrdersOnly})
