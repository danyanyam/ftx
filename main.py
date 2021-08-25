from datetime import datetime
import os
import asyncio
import datetime as dt
from pprint import pprint

from library.ftx.account import Account
from library.ftx.futures import Futures


async def main():
    acc = Account(os.getenv('FTX_API'), os.getenv('FTX_API_SECRET'))
    fut = Futures(os.getenv('FTX_API'), os.getenv('FTX_API_SECRET'))

    info = await acc.get_account_information()


if __name__ == "__main__":
    asyncio.run(main())
