import time
import json
import hmac
import asyncio
import websockets

from library.logging import logger


class DataListener:
    endpoint = 'wss://ftx.com/ws/'

    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.subscriptions = []

        self._orders = asyncio.Queue()

    @logger.catch
    async def listen(self):
        """ Listens to subscribed data streams """

        async with websockets.connect(self.endpoint) as client:

            # Authenticating in websocket server
            await client.send(self._prepare_authentication())
            # Subscribing for channels
            await self._execute_orders(client)

            while len(self.subscriptions) > 0:
                yield json.loads(await client.recv())

                # Unsubscribing from channels, if needed
                await self._execute_orders(client)

    async def subscribe(self, channel: str, market: str) -> None:
        """ Subscribes to real-time data stream """
        assert channel in ('orderbook', 'trades', 'ticker')

        if (channel, market) not in self.subscriptions:
            self.subscriptions.append((channel, market))
            await self._orders.put(self._to_ws_format(op='subscribe', channel=channel, market=market))
            print(f'Subscribed to {market} - {channel}')

    async def unsubscribe(self, channel: str, market: str) -> None:
        """ Unsubscribes from real-time data stream """
        if (channel, market) in self.subscriptions:
            self.subscriptions.remove((channel, market))
            await self._orders.put(self._to_ws_format(op='unsubscribe', channel=channel, market=market))
            print(f'Unsubscribed from {market} - {channel}')

    async def _execute_orders(self, client):
        """ execute orders if the appear in queue  """
        if self._orders.qsize() > 0:
            await client.send(await self._orders.get())

    def _prepare_authentication(self):
        """ before subscribing to channels, we need to
        identify ourselves by passing signed headers """
        ts = int(time.time() * 1000)
        return self._to_ws_format(op='login', args={'key': self.api_key, 'sign': hmac.new(self.api_secret.encode(), f'{ts}websocket_login'.encode(), 'sha256').hexdigest(), 'time': ts})

    def _to_ws_format(self, **kwargs):
        """ Sending dictionaries must be dumped to string
        end encoded. This function also adds pythonic way
        of passing arguments """
        return json.dumps(kwargs).encode()
