
import os
import asyncio

from library.ftx.asyncronous.websocket import DataListener


async def main():
    dl = DataListener(os.getenv('FTX_API'), os.getenv('FTX_API_SECRET'))

    r = await dl.subscribe('trades', 'BTC-PERP')
    r = await dl.subscribe('trades', 'ETH-PERP')

    async for message in dl.listen():
        print(message)


if __name__ == "__main__":
    asyncio.run(main())



