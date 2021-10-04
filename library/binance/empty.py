from config import api_key, secret
from wallet import Wallet
from subaccount import Subaccount
from market import Market
from spot import Spot
from margin import Margin
from savings import Savings
from mining import Mining
from futures import Futures
from btvt import BLVT
from bsswap import BSSwap
from fiat import Fiat
import asyncio
from pprint import pprint

wallet = Wallet(api_key, secret)
subaccaount = Subaccount(api_key, secret)
market = Market(api_key, secret)
spot = Spot(api_key, secret)
margin = Margin(api_key, secret)
savings = Savings(api_key, secret)
mining = Mining(api_key, secret)
futures = Futures(api_key, secret)
btlv = BLVT(api_key, secret)
bsswap = BSSwap(api_key, secret)
fiat = Fiat(api_key, secret)
# pprint(asyncio.run(savings.get_fixed_and_activity_product_list(asset="USDT")))
# pprint(asyncio.run(futures.new_future_account_transfer()))
pprint(asyncio.run(fiat.get_fiat_deposit_withdraw_history()))