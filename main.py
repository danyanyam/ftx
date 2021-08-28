import os
import asyncio

from library.ftx.websocket import DataListener


async def main():

    ws = DataListener(os.getenv('FTX_API'), os.getenv('FTX_API_SECRET'))
    await ws.subscribe(channel='ticker', market='BTC-PERP')

    async for message in ws.listen():
        print(message)


if __name__ == "__main__":
    asyncio.run(main())
