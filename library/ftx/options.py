import datetime as dt
from library.ftx.base import BaseApiClass


# TODO create_quote_request -> expiry assert

class Orders(BaseApiClass):
    """docstring for Orders."""

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name)

    def list_quote_requests(self):
        """ https://docs.ftx.com/#list-quote-requests """
        return self.get('/api/options/requests', authentication_required=False)

    def my_quote_requests(self):
        """ https://docs.ftx.com/#your-quote-requests """
        return self.get('/api/options/my_requests')

    def create_quote_request(self, underlying: str, type: str, strike: float, expiry: dt.datetime, side: str, size: float, limitPrice: float = None, hideLimitPrice: bool = True, requestExpiry: dt.datetime = None, counterpartyId: int = None):
        """ https://docs.ftx.com/#create-quote-requests """
        return self.post('/api/options/requests', data={'underlying': underlying, 'type': type, 'strike': strike, 'expiry': expiry, 'side': side, 'size': size, 'limitPrice': limitPrice, 'hideLimitPrice': hideLimitPrice, 'requestExpiry': requestExpiry, 'counterpartyId': counterpartyId})

    def cancel_quote_request(self, request_id: int):
        """ https://docs.ftx.com/#cancel-quote-request """
        return self.delete(f'/api/options/requests/{request_id}')

    def get_quotes_for_quote_request(self, request_id: int):
        """ https://docs.ftx.com/#get-quotes-for-your-quote-request """
        return self.get(f'/api/options/requests/{request_id}/quotes')

    def create_quote(self, request_id: int, price: float):
        """ https://docs.ftx.com/#create-quote """
        return self.post(f'/api/options/requests/{request_id}/quotes', data={'price': price})

    def get_my_quotes(self):
        """ https://docs.ftx.com/#get-my-quotes """
        return self.post(f'/api/options/my_quotes')

    def cancel_quote(self, quote_id: int):
        """ https://docs.ftx.com/#cancel-quote """
        return self.delete(f'/api/options/quotes/{quote_id}')

    def accept_options_quote(self, quote_id: int):
        """ https://docs.ftx.com/#accept-options-quote """
        return self.post(f'/api/options/quotes/{quote_id}/accept')

    def get_account_options_info(self):
        """ https://docs.ftx.com/#get-account-options-info """
        return self.get(f'/api/options/account_info')

    def get_options_positions(self):
        """ https://docs.ftx.com/#get-options-positions """
        return self.get(f'/api/options/positions')

    def get_public_options_trades(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-public-options-trades """
        return self.get(f'/api/options/trades', start_time=start_time, end_time=end_time)

    def get_options_fills(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-options-fills """
        return self.get(f'/api/options/fills', start_time=start_time, end_time=end_time)

    def get_24h_options_volume(self):
        """ https://docs.ftx.com/#get-24h-option-volume """
        return self.get(f'/api/stats/24h_options_volume')

    def get_option_open_interest_hist_vol(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-option-open-interest """
        return self.get(f'/api/options/historical_volumes/BTC', start_time=start_time, end_time=end_time)

    def get_option_open_interest_hist(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-option-open-interest """
        return self.get(f'/api/options/historical_open_interest/BTC', start_time=start_time, end_time=end_time)

    def get_option_open_interest(self):
        """ https://docs.ftx.com/#get-option-open-interest-2 """
        return self.get(f'/api/options/open_interest/BTC')
