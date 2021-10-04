from library.ftx.base import BaseApiClass


class Convert(BaseApiClass):
    """docstring for Fills."""

    def __init__(self, api_key: str, secret_key: str, subaccount_name: str = ''):
        super().__init__(api_key, secret_key, subaccount_name)

    def request_quote(self, fromCoin: str, toCoin: str, size: float):
        """ https://docs.ftx.com/#request-quote """
        return self.post('/api/otc/quotes', data={'fromCoin': fromCoin, 'toCoin': toCoin, 'size': size})

    def get_quote_status(self, quoteId: str, market: str = ''):
        """ https://docs.ftx.com/#get-quote-status """
        return self.get(f'/api/quotes/{quoteId}', market=market)

    def accept_quote(self, quoteId: int):
        """ https://docs.ftx.com/#accept-quote """
        return self.post(f'/api/otc/quotes/{quoteId}/accept')