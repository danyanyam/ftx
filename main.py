import os
import asyncio
from pprint import pprint

from library.ftx.account import Account


async def main():
    acc = Account(os.getenv('FTX_API'), os.getenv('FTX_API_SECRET'))
    info = await acc.get_account_information()
    pprint(info)


if __name__ == "__main__":
    asyncio.run(main())
