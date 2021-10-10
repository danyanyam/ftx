from abc import ABC, abstractmethod
from typing import Tuple, List
import datetime as dt
from dataclasses import dataclass
from glob import glob
import csv
import os

from .events import MarketEvent


@dataclass
class Bar:
    symbol: str
    dt: dt.datetime
    open: float
    low: float
    high: float
    close: float
    volume: float


class DataHandler(ABC):
    """
    DataHandler is an abstract base class providing an interface for
    all subsequent (inherited) data handlers (both live and historic).

    The goal of a (derived) DataHandler object is to output a generated
    set of bars (OLHCVI) for each symbol requested.

    This will replicate how a live strategy would function as current
    market data would be sent "down the pipe". Thus a historic and live
    system will be treated identically by the rest of the backtesting suite.
    """

    @abstractmethod
    def get_latest_bars(
        self, symbol: str, n: int = 1
    ) -> List[Bar]:
        """
        Returns the last N bars from the latest_symbol list,
        or fewer if less bars are available.

        returns (sybmbol, datetime, open, low, high, close, volume).
        """
        raise NotImplementedError("Should implement get_latest_bars()")

    @abstractmethod
    def update_bars(self) -> None:
        """
        Pushes the latest bar to the latest symbol structure
        for all symbols in the symbol list.
        """
        raise NotImplementedError("Should implement update_bars()")


class FtxHistoricCSVDataHandler(DataHandler):
    """
    HistoricCSVDataHandler is designed to read CSV files for
    each requested symbol from disk and provide an interface
    to obtain the "latest" bar in a manner identical to a live
    trading interface.
    """

    def __init__(self, events, csv_dir, symbol_list):
        """
        Initialises the historic data handler by requesting the location of the
        CSV files and a list of symbols.

        It will be assumed that all files are of the form 'symbol.csv', where
        symbol is a string in the list.

        Parameters:
            events - The Event Queue.
            csv_dir - Absolute directory path to the CSV files.
            symbol_list - A list of symbol strings.
        """

        self.events = events
        self.csv_dir = csv_dir
        self.symbol_list = symbol_list

        # {'btcusdt': [(2021-01-01 13:52:06, ...), ...]}
        self.symbol_data = {}
        self.latest_symbol_data = {}
        self.continue_backtest = True

        self._open_convert_csv_files()
        self.first_time = True
        self.iterators = self._init_iterators()

    def _open_convert_csv_files(self) -> None:

        for symbol in self.symbol_list:

            path = os.path.join(self.csv_dir, symbol + '.csv')

            if not os.path.exists(path):
                continue

            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                bars_list = []
                for bar in reader:
                    bars_list.append(
                        Bar(symbol=symbol,
                            dt=dt.datetime.strptime(bar['startTime'],
                                                    '%Y-%m-%dT%H:%M:%S%z').replace(tzinfo=None),
                            open=float(bar['open']),
                            close=float(bar['close']),
                            low=float(bar['low']),
                            volume=float(bar['volume']),
                            high=float(bar['high'])))

            self.symbol_data[symbol] = bars_list
            self.latest_symbol_data[symbol] = bars_list.copy()

        # self.symbol_data[symbol] = ...

    def _init_iterators(self):
        iterators = {}
        for symbol in self.symbol_list:
            iterators[symbol] = self._get_new_bar(symbol)
        return iterators

    def _get_new_bar(self, symbol: str) -> Bar:
        """
        Returns the latest bar from the data feed as a tuple of
        (sybmbol, datetime, open, low, high, close, volume).
        """


        for bar in self.symbol_data[symbol]:
            yield bar


    def get_latest_bars(self, symbol: str, n=1) -> List[Bar]:
        """
        Returns the last N bars from the latest_symbol list,
        or N-k if less available.
        """
        assert symbol in self.latest_symbol_data.keys(), \
            f'{symbol=} is not available'

        bar_list = self.latest_symbol_data[symbol]
        return bar_list[-n:]

    def update_bars(self) -> None:
        """
        Pushes the latest bar to the latest_symbol_data structure
        for all symbols in the symbol list.
        """
        bar = None

        for symbol in self.symbol_list:
            try:

                bar = next(self.iterators[symbol])
                print(bar)

            except StopIteration:
                self.continue_backtest = False


            if bar is not None:

                self.latest_symbol_data[symbol].append(bar)

        self.events.put(MarketEvent())
