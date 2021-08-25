from datetime import datetime
import os
import asyncio
import datetime as dt
from pprint import pprint

from library.ftx.account import Account
from library.ftx.futures import Futures
from library.ftx.orders import Orders


async def main():
    acc = Account(os.getenv('FTX_API'), os.getenv('FTX_API_SECRET'))
    fut = Futures(os.getenv('FTX_API'), os.getenv('FTX_API_SECRET'))
    ord = Orders(os.getenv('FTX_API'), os.getenv('FTX_API_SECRET'))

    # info = await ord.get_order_history(start_time=dt.datetime(2020, 1, 1), end_time=dt.datetime(2021, 1, 1))
    info = await ord.get_open_trigger_orders(market='BTC-PERP', type_='stop')
    # info = await acc.get_account_information()
    pprint(info)

if __name__ == "__main__":
    asyncio.run(main())
