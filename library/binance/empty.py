from config import api_key, secret
from wallet import Wallet
from subaccount import Subaccount
from market import Market
import asyncio
from pprint import pprint

wallet = Wallet(api_key, secret)
subaccaount = Subaccount(api_key, secret)
market = Market(api_key, secret)
pprint(asyncio.run(market.symbol_order_book_ticker()))
