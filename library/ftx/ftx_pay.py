import datetime as dt
from library.ftx.base import BaseApiClass


class FTXPay(BaseApiClass):
    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name)

    def get_app_details_and_payments(self, user_specific_id: int, start_time: dt.datetime = None, end_time: dt.datetime = None, limit: int = None):
        return self.get(f'/api/ftxpay/apps/{user_specific_id}/details', start_time=start_time, end_time=end_time, limit=limit)

    def create_order(self, coin: str, size: float, allowTip: bool = True, clientId: str = None, notes: str = None,  user_specific_id: int = None, app_id: int = None):
        assert any((user_specific_id, app_id)) and not all((user_specific_id, app_id)), f'either user_specific_id or app_id'
        link = f'/api/ftxpay/apps/{user_specific_id}/orders_by_usid' if user_specific_id else f'/ftxpay/apps/{app_id}/orders'
        return self.post(link, data={'coin': coin, 'size': size, 'allowTip': allowTip, 'clientId': clientId, 'notes': notes})

    def get_orders(self, user_specific_id: int = None, app_id: int = None,  start_time: dt.datetime = None, end_time: dt.datetime = None):
        assert any((user_specific_id, app_id)) and not all((user_specific_id, app_id)), f'either user_specific_id or app_id'
        link = f'/api/ftxpay/apps/{user_specific_id}/orders_by_usid' if user_specific_id else f'/ftxpay/apps/{app_id}/orders'
        return self.get(link, start_time=start_time, end_time=end_time)

    def cancel_orders(self, order_id: int, user_specific_id: int = None, app_id: int = None):
        assert any((user_specific_id, app_id)) and not all((user_specific_id, app_id)), f'either user_specific_id or app_id'
        link = f'/api/ftxpay/apps/{user_specific_id}/{order_id}orders_by_usid' if user_specific_id else f'/ftxpay/apps/{app_id}/{order_id}/orders'
        return self.delete(link)

    def return_payment(self, app_id: int, payment_id: int, size: float = None):
        return self.post(f'/api/ftxpay/{app_id}/{payment_id}/return', data={'size': size})
