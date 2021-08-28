import datetime as dt
from library.ftx.base import BaseApiClass


# TODO create_quote_request -> expiry assert

class Orders(BaseApiClass):
    """docstring for Orders."""

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name)

    async def list_quote_requests(self):
        """ https://docs.ftx.com/#list-quote-requests """
        return await self.get('/api/options/requests', authentication_required=False)

    async def my_quote_requests(self):
        """ https://docs.ftx.com/#your-quote-requests """
        return await self.get('/api/options/my_requests')

    async def create_quote_request(self, underlying: str, type: str, strike: float, expiry: dt.datetime, side: str, size: float, limitPrice: float = None, hideLimitPrice: bool = True, requestExpiry: dt.datetime = None, counterpartyId: int = None):
        """ https://docs.ftx.com/#create-quote-requests """
        return await self.post('/api/options/requests', data={'underlying': underlying, 'type': type, 'strike': strike, 'expiry': expiry, 'side': side, 'size': size, 'limitPrice': limitPrice, 'hideLimitPrice': hideLimitPrice, 'requestExpiry': requestExpiry, 'counterpartyId': counterpartyId})

    async def cancel_quote_request(self, request_id: int):
        """ https://docs.ftx.com/#cancel-quote-request """
        return await self.delete(f'/api/options/requests/{request_id}')

    async def get_quotes_for_quote_request(self, request_id: int):
        """ https://docs.ftx.com/#get-quotes-for-your-quote-request """
        return await self.get(f'/api/options/requests/{request_id}/quotes')

    async def create_quote(self, request_id: int, price: float):
        """ https://docs.ftx.com/#create-quote """
        return await self.post(f'/api/options/requests/{request_id}/quotes', data={'price': price})

    async def get_my_quotes(self):
        """ https://docs.ftx.com/#get-my-quotes """
        return await self.post(f'/api/options/my_quotes')

    async def cancel_quote(self, quote_id: int):
        """ https://docs.ftx.com/#cancel-quote """
        return await self.delete(f'/api/options/quotes/{quote_id}')

    async def accept_options_quote(self, quote_id: int):
        """ https://docs.ftx.com/#accept-options-quote """
        return await self.post(f'/api/options/quotes/{quote_id}/accept')

    async def get_account_options_info(self):
        """ https://docs.ftx.com/#get-account-options-info """
        return await self.get(f'/api/options/account_info')

    async def get_options_positions(self):
        """ https://docs.ftx.com/#get-options-positions """
        return await self.get(f'/api/options/positions')

    async def get_public_options_trades(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-public-options-trades """
        return await self.get(f'/api/options/trades', start_time=start_time, end_time=end_time)

    async def get_options_fills(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-options-fills """
        return await self.get(f'/api/options/fills', start_time=start_time, end_time=end_time)

    async def get_24h_options_volume(self):
        """ https://docs.ftx.com/#get-24h-option-volume """
        return await self.get(f'/api/stats/24h_options_volume')

    async def get_option_open_interest_hist_vol(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-option-open-interest """
        return await self.get(f'/api/options/historical_volumes/BTC', start_time=start_time, end_time=end_time)

    async def get_option_open_interest_hist(self, start_time: dt.datetime = None, end_time: dt.datetime = None):
        """ https://docs.ftx.com/#get-option-open-interest """
        return await self.get(f'/api/options/historical_open_interest/BTC', start_time=start_time, end_time=end_time)

    async def get_option_open_interest(self):
        """ https://docs.ftx.com/#get-option-open-interest-2 """
        return await self.get(f'/api/options/open_interest/BTC')
