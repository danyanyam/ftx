from abc import ABC, abstractmethod
from math import floor
import datetime as dt
from typing import Dict, List
import pandas as pd

from .events import FillEvent, OrderEvent
from .enums import EventTypes, SignalTypes
from .data import DataHandler
from .enums import OrderTypes
from .events import SignalEvent


class Portfolio(ABC):
    """
    The Portfolio class handles the positions and market value of all
    instruments at a resolution of a "bar", i.e. secondly, minutely, 5-min,
    30-min, 60 min or EOD.
    """

    @abstractmethod
    def update_signal(self, event: EventTypes):
        """
        Acts on a SignalEvent to generate new orders based on the portfolio
        logic.
        """
        raise NotImplementedError("Should implement update_signal()")

    @abstractmethod
    def update_fill(self, event: EventTypes):
        """
        Updates the portfolio current positions and holdings from a FillEvent.
        """
        raise NotImplementedError("Should implement update_fill()")


class NaivePortfolio(Portfolio):
    """
    The NaivePortfolio object is designed to send orders to a brokerage object
    with a constant quantity size blindly, i.e. without any risk management or
    position sizing. It is used to test simpler strategies such as
    BuyAndHoldStrategy.
    """

    def __init__(self, bars: DataHandler, events: EventTypes,
                 start_date: dt.datetime, initial_capital=100_000):

        self.bars = bars
        self.events = events
        self.symbol_list = bars.symbol_list
        self.start_date = start_date
        self.initial_capital = initial_capital

        self.all_positions = self.construct_all_positions()
        self.current_positions = {symbol: 0 for symbol in self.symbol_list}

        self.all_holdings = self.construct_all_holdings()
        self.current_holdings = self.construct_current_holdings()

    def construct_all_positions(self) -> List[Dict[str, str]]:
        """
        Constructs the positions list using the start_date to determine when
        the time index will begin.
        """
        d = {symbol: 0 for symbol in self.symbol_list}
        d['datetime'] = self.start_date
        return [d]

    def construct_all_holdings(self) -> List[Dict[str, str]]:
        """
        Constructs the holdings list using the start_date to determine when the
        time index will begin.
        """
        d = {symbol: 0 for symbol in self.symbol_list}
        d['datetime'] = self.start_date
        d['cash'] = self.initial_capital
        d['commission'] = 0.0
        d['total'] = self.initial_capital
        return [d]

    def construct_current_holdings(self) -> Dict[str, str]:
        """
        This constructs the dictionary which will hold the instantaneous
        value of the portfolio across all symbols.
        """
        d = {symbol: 0 for symbol in self.symbol_list}
        d['cash'] = self.initial_capital
        d['commission'] = 0.0
        d['total'] = self.initial_capital
        return d

    def update_timeindex(self, event: EventTypes) -> None:
        """
        Adds a new record to the positions matrix for the current
        market data bar. This reflects the PREVIOUS bar, i.e. all
        current market data at this stage is known (OLHCVI).

        Makes use of a MarketEvent from the events queue.
        """

        bars = {}
        for symbol in self.symbol_list:
            bars[symbol] = self.bars.get_latest_bars(symbol, n=1)

        # Update positions

        positions = {symbol: 0 for symbol in self.symbol_list}
        positions['datetime'] = bars[self.symbol_list[0]][0].dt

        for symbol in self.symbol_list:
            positions[symbol] = self.current_positions[symbol]

        # Append the current positions
        self.all_positions.append(positions)

        # Update holdings
        holdings = {symbol: 0 for symbol in self.symbol_list}
        holdings['datetime'] = bars[self.symbol_list[0]][0].dt
        holdings['cash'] = self.current_holdings['cash']
        holdings['commission'] = self.current_holdings['commission']
        holdings['total'] = self.current_holdings['cash']

        for symbol in self.symbol_list:
            # Approximation to the real value
            market_value = self.current_positions[symbol] * bars[symbol][0].close
            holdings[symbol] = market_value
            holdings['total'] += market_value

        # Append the current holdings
        self.all_holdings.append(holdings)

    def update_positions_from_fill(self, fill: FillEvent) -> None:
        """
        Takes a FillEvent object and updates the position matrix
        to reflect the new position.

        Parameters:
        fill - The FillEvent object to update the positions with.
        """
        # Check whether the fill is a buy or sell
        fill_direction = fill.direction.value

        # Update positions list with new quantities
        self.current_positions[fill.symbol] += fill_direction * fill.quantity

    def update_holdings_from_fill(self, fill: FillEvent) -> None:
        """
        Takes a FillEvent object and updates the holdings matrix
        to reflect the holdings value.

        Parameters:
        fill - The FillEvent object to update the holdings with.
        """
        # Check whether the fill is a buy or sell
        fill_dir = fill.direction.value

        # Update holdings list with new quantities
        fill_cost = self.bars.get_latest_bars(fill.symbol)[0].close
        cost = fill_dir * fill_cost * fill.quantity
        self.current_holdings[fill.symbol] += cost
        self.current_holdings['commission'] += fill.commission
        self.current_holdings['cash'] -= (cost + fill.commission)
        self.current_holdings['total'] -= (cost + fill.commission)

    def generate_naive_order(self, signal: SignalEvent) -> OrderEvent:
        """
        Simply transacts an OrderEvent object as a constant quantity
        sizing of the signal object, without risk management or
        position sizing considerations.

        Parameters:
        signal - The SignalEvent signal information.
        """

        order = None

        symbol = signal.symbol
        direction = signal.signal_type
        strength = signal.strength

        mkt_quantity = floor(100 * strength)
        cur_quantity = self.current_positions[symbol]
        order_type = OrderTypes.MARKET

        if direction == SignalTypes.BUY and cur_quantity == 0:
            order = OrderEvent(
                symbol, order_type, mkt_quantity, SignalTypes.BUY)

        elif direction == SignalTypes.SELL and cur_quantity == 0:
            order = OrderEvent(
                symbol, order_type, mkt_quantity, SignalTypes.SELL)

        elif direction == SignalTypes.EXIT and cur_quantity > 0:
            order = OrderEvent(
                symbol, order_type, abs(cur_quantity), SignalTypes.SELL)

        elif direction == SignalTypes and cur_quantity < 0:
            order = OrderEvent(
                symbol, order_type, abs(cur_quantity), SignalTypes.BUY)

        return order

    def create_equity_curve_dataframe(self) -> None:
        """
        Creates a pandas DataFrame from the all_holdings
        list of dictionaries.
        """
        curve = pd.DataFrame(self.all_holdings)
        curve.set_index('datetime', inplace=True)
        curve['returns'] = curve['total'].pct_change()
        curve['equity_curve'] = (1 + curve['returns']).cumprod()
        return curve

    def update_signal(self, event: EventTypes) -> None:
        """
        Acts on a SignalEvent to generate new orders
        based on the portfolio logic.
        """
        if event.type == EventTypes.SIGNAL:
            order_event = self.generate_naive_order(event)
            self.events.put(order_event)

    def update_fill(self, event: EventTypes) -> None:
        """
        Updates the portfolio current positions and holdings
        from a FillEvent.
        """
        if event.type == EventTypes.FILL:
            self.update_positions_from_fill(event)
            self.update_holdings_from_fill(event)
