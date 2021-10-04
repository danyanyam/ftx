import simplefix as fix
import asyncio
import websockets
import ssl

class Fix:

    endpoint = 'tcp+ssl://fix.ftx.com:4363'


async def main():
    async with websockets.connect('wss://fix.ftx.com:4363') as client:
        await client.send('8=FIX.4.2|9=162|35=A|49=zyfvB4QPg0A3kkVgqUE9V1fOA-Y6jhdG3seqIIZx|56=FTX')
        print(await client.recv())



if __name__ == "__main__":
    asyncio.run(main())