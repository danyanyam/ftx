from config import api_key, secret_key
from account import Wallet

wallet = Wallet(api_key, secret_key)
wallet.enable_fast_withdraw_switch()
