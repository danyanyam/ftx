import time
import json
import hmac
import asyncio
import websockets

from library.logging import logger
from library.ftx.markets import Markets


class DataListener:
    endpoint = 'wss://ftx.com/ws/'
    channels = ('orderbook', 'trades', 'ticker')

    def __init__(self, api_key: str, api_secret: str):
        assert api_key and api_secret, f'keys may not be empty, received types {type(api_key)}, {type(api_secret)}'

        self.api_key = api_key
        self.api_secret = api_secret
        self._subscriptions = []

        self.__orders = asyncio.Queue()

        # for retreiving universe of possible assets
        self._markets = Markets(api_key, api_secret)

    # @logger.catch
    async def listen(self):
        """ Listens to subscribed data streams """

        async with websockets.connect(self.endpoint) as client:

            # Authenticating in websocket server
            await client.send(self._prepare_authentication())
            # Subscribing for channels
            await self._execute_orders_from_queue(client)

            while len(self._subscriptions) > 0:
                yield json.loads(await client.recv())

                # Unsubscribing from channels, if needed
                await self._execute_orders_from_queue(client)

    async def subscribe(self, channel: str, market: str) -> None:
        """ Subscribes to real-time data stream """
        assert channel in ('orderbook', 'trades', 'ticker')

        if (channel, market) not in self._subscriptions:
            self._subscriptions.append((channel, market))
            await self.__orders.put(self._to_ws_format(op='subscribe', channel=channel, market=market))
            print(f'Subscribed to {market} - {channel}')

    async def unsubscribe(self, channel: str, market: str) -> None:
        """ Unsubscribes from real-time data stream """
        if (channel, market) in self._subscriptions:
            self._subscriptions.remove((channel, market))
            await self.__orders.put(self._to_ws_format(op='unsubscribe', channel=channel, market=market))
            print(f'Unsubscribed from {market} - {channel}')

    async def _execute_orders_from_queue(self, client):
        """ execute orders if the appear in queue  """
        if self.__orders.qsize() > 0:
            await client.send(await self.__orders.get())

    @property
    def subscriptions(self):
        """ This is done to prevent subscriptions
        from changing via method accessing """
        return self._subscriptions

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

    async def markets(self, name_only: bool = True):
        server_response =  await self._markets.get_markets()
        if server_response.get('success'):
            return tuple(i['name'] for i in server_response['result']) if name_only else tuple(server_response['result'])


