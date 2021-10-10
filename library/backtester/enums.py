from enum import Enum


class SignalTypes(Enum):
    BUY = 1
    EXIT = 0
    SELL = -1


class EventTypes(Enum):
    MARKET = 'MARKET'
    SIGNAL = 'SIGNAL'
    ORDER = 'ORDER'
    FILL = 'FILL'


class OrderTypes(Enum):
    MARKET = 0
    LIMIT = 1
    MAKER = 2
