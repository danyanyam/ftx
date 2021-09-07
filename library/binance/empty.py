from config import api_key, secret
from wallet import Wallet
from subaccount import Subaccount
from market import Market
from spot import Spot
from margin import Margin
from savings import Savings
import asyncio
from pprint import pprint

wallet = Wallet(api_key, secret)
subaccaount = Subaccount(api_key, secret)
market = Market(api_key, secret)
spot = Spot(api_key, secret)
margin = Margin(api_key, secret)
savings = Savings(api_key, secret)

pprint(asyncio.run(savings.get_fixed_and_activity_product_list(asset="USDT")))
# pprint(asyncio.run(savings.account_information()))