from config import api_key, secret
from wallet import Wallet
import asyncio
from pprint import pprint

wallet = Wallet(api_key, secret)
pprint(asyncio.run(wallet.api_key_permission()))
