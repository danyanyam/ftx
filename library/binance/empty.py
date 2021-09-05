from config import api_key, secret
from wallet import Wallet
from subaccount import Subaccount
from market import Market
from spot import Spot
import asyncio
from pprint import pprint

wallet = Wallet(api_key, secret)
subaccaount = Subaccount(api_key, secret)
market = Market(api_key, secret)
spot = Spot(api_key, secret)

pprint(asyncio.run(spot.account_information()))

# pprint(asyncio.run(spot.account_trade_list()))

# pprint(asyncio.run(spot.cancel_all_orders()))
# pprint(asyncio.run(market.exchange_information(symbol='BTCUSDT')))
# pprint(asyncio.run(market.symbol_price_ticker(symbol='BTCUSDT')))
