from enum import Enum


class Interval(Enum):
    ONE_MINUTE = '1m'


def check(interval):

    if not isinstance(interval, Interval):
        raise TypeError(f'Bad interval value: {interval}')


def pass_agruments(a: str = None,
                   b: str = None,
                   c: str = None,
                   d: str = None):
    return
# assert interval in ['1m', '3m', '5m', '15m', '30m', '1h', '2h',
#                             '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']
