from os import symlink
from base import BaseApiClass
import datetime as dt


class Market(BaseApiClass):
    """https://binance-docs.github.io/apidocs/spot/en/#market-data-endpoints"""

    def __init__(self, api_key: str, secret_key: str):
        super().__init__(api_key, secret_key)

    def test_connectivity(self):
        """https://binance-docs.github.io/apidocs/spot/en/#test-connectivity"""
        return self.get('/api/v3/ping')

    # TODO: Complete the function
    def exchange_information(self):
        """https://binance-docs.github.io/apidocs/spot/en/#exchange-information"""
        # pass
        return self.get('/api/v3/exchangeInfo', symbol='BTCUSDT')

    def order_book(self,
                   symbol: str = 'BTCUSDT',
                   limit: int = 100):
        """https://binance-docs.github.io/apidocs/spot/en/#order-book"""
        assert limit in [5, 10, 20, 50, 100, 500, 1000, 5000], f"Limit {limit} is not in possible values"
        return self.get('/api/v3/depth', symbol=symbol, limit=limit)

    def recent_trade_list(self,
                          symbol: str = 'BTCUSDT',
                          limit: int = 100):
        """https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list"""
        assert limit <= 1000, f"Limit {limit} is too high. Maximum value is 1000"
        return self.get('/api/v3/trades', symbol=symbol, limit=limit)

    def old_trade_lookup(self,
                         symbol: str = 'BTCUSDT',
                         limit: int = 100,
                         fromId: int = None):
        """https://binance-docs.github.io/apidocs/spot/en/#old-trade-lookup-market_data"""
        return self.get('/api/v3/historicalTrades', symbol=symbol, limit=limit, fromId=fromId)

    def comp_agg_trades_list(self,
                             symbol: str = 'BTCUSDT',
                             fromId: int = None,
                             start_time: dt.datetime = None,
                             end_time: dt.datetime = None,
                             limit: int = None):
        """https://binance-docs.github.io/apidocs/spot/en/#compressed-aggregate-trades-list
        [
            {
            "a": 26129,         // Aggregate tradeId
            "p": "0.01633102",  // Price
            "q": "4.70443515",  // Quantity
            "f": 27781,         // First tradeId
            "l": 27781,         // Last tradeId
            "T": 1498793709153, // Timestamp
            "m": true,          // Was the buyer the maker?
            "M": true           // Was the trade the best price match?
            }
        ]
        """
        return self.get('/api/v3/aggTrades', symbol=symbol, fromId=fromId, start_time=start_time, end_time=end_time, limit=limit)

    def candlestick(self,
                    symbol: str = 'BTCUSDT',
                    interval: str = '3d',
                    start_time: dt.datetime = None,
                    end_time: dt.datetime = None,
                    limit: int = None):
        """https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data"""
        assert interval in ['1m', '3m', '5m', '15m', '30m', '1h', '2h',
                            '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M'], f"Interval {interval} is not in possible values"
        return self.get('/api/v3/klines', symbol=symbol, interval=interval, start_time=start_time, end_time=end_time, limit=limit)

    def current_average_price(self,
                              symbol: str = 'BTCUSDT'):
        """https://binance-docs.github.io/apidocs/spot/en/#current-average-price"""
        return self.get('/api/v3/avgPrice', symbol=symbol)

    def day_ticket_price_change(self,
                                symbol: str = None):
        """https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics"""
        return self.get('/api/v3/ticker/24hr', symbol=symbol)

    def symbol_price_ticker(self,
                            symbol: str = None):
        """https://binance-docs.github.io/apidocs/spot/en/#symbol-price-ticker"""
        return self.get('/api/v3/ticker/price', symbol=symbol)

    def symbol_order_book_ticker(self,
                                 symbol: str = None):
        """https://binance-docs.github.io/apidocs/spot/en/#symbol-order-book-ticker"""
        return self.get('/api/v3/ticker/bookTicker', symbol=symbol)
