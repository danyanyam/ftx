import datetime as dt
from abc import ABC, abstractmethod
from typing import Dict

from .events import SignalEvent
from .enums import EventTypes, SignalTypes
from .data import DataHandler


class Strategy(ABC):
    """
    Strategy is an abstract base class providing an interface for
    all subsequent (inherited) strategy handling objects.

    The goal of a (derived) Strategy object is to generate Signal
    objects for particular symbols based on the inputs of Bars
    (OLHCVI) generated by a DataHandler object.

    This is designed to work both with historic and live data as
    the Strategy object is agnostic to the data source,
    since it obtains the bar tuples from a queue object.
    """

    @abstractmethod
    def calculate_signals(self) -> None:
        """ Provides the mechanisms to calculate the list of signals.  """
        return NotImplementedError('Should implement calculate_signals()')


class BuyAndHoldStrategy(Strategy):
    """
    This is an extremely simple strategy that goes LONG all of the
    symbols as soon as a bar is received. It will never exit a position.

    It is primarily used as a testing mechanism for the Strategy class
    as well as a benchmark upon which to compare other strategies.
    """

    def __init__(self, bars: DataHandler, events: EventTypes):
        """
        Parameters:
            bars - The DataHandler object that provides bar information
            events - The Event Queue object.
        """
        self.bars = bars
        self.events = events
        self.symbol_list = bars.symbol_list

        # Once buy & hold signal is given, these are set to True
        self.bought = self._calculate_initial_bought()

    def _calculate_initial_bought(self) -> Dict[str, bool]:
        """
        Adds keys to the bought dictionary for all symbols and sets them
        to False.
        """
        return {symbol: False for symbol in self.symbol_list}

    def calculate_signals(self, event: EventTypes) -> None:
        """
        For "Buy and Hold" we generate a single signal per symbol and then no
        additional signals. This means we are constantly long the market from
        the date of strategy initialisation.

        Parameters
        event - A MarketEvent object.
        """
        if not event.type == EventTypes.MARKET:
            return

        for symbol in self.symbol_list:
            bar = self.bars.get_latest_bars(symbol, n=1)
            if bar is not None:
                if self.bought[symbol] == False:
                    # (Symbol, Datetime, Type = LONG, SHORT or EXIT)
                    bar = bar[0]
                    signal = SignalEvent(bar.symbol, bar.dt, SignalTypes.BUY)
                    self.events.put(signal)
                    self.bought[symbol] = True