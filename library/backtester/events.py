import datetime as dt
from .enums import EventTypes, SignalTypes, OrderTypes


class Event:
    """
    Event is base class providing an interface for all subsequent
    (inherited) events, that will trigger further events in the
    trading infrastructure.
    """
    pass


class MarketEvent(Event):
    """
    This is triggered when the outer while loop begins a new "heartbeat".
    It occurs when the DataHandler object receives a new update of market
    data for any symbols which are currently being tracked. It is used to
    trigger the Strategy object generating new trading signals. The event
    object simply contains an identification that it is a market event,
    with no other structure.

    Handles the event of receiving a new market update with
    corresponding bars.
    """

    def __init__(self):
        self.type = EventTypes.MARKET


class SignalEvent(Event):
    """
    The Strategy object utilises market data to create new SignalEvents.
    The SignalEvent contains a ticker symbol, a timestamp for when it was
    generated and a direction (long or short). The SignalEvents are utilised
    by the Portfolio object as advice for how to trade.

    Handles the event of sending a Signal from a Strategy object.
    This is received by a Portfolio object and acted upon.
    """

    def __init__(self, symbol: str, datetime: dt.datetime, type: SignalTypes):
        """
        Parameters:
            symbol (str): The ticker symbol, e.g. 'BTCUSD'.
            datetime (dt.datetime): The timestamp, when the signal was
        generated
            type (SignalTypes): 'BUY' or 'SELL'
        """
        self.type = EventTypes.SIGNAL
        self.symbol = symbol
        self.dt = datetime
        self.signal_type = type
        self.strength = 0.01


class OrderEvent(Event):
    """
    When a Portfolio object receives SignalEvents it assesses them in the
    wider context of the portfolio, in terms of risk and position sizing.
    This ultimately leads to OrderEvents that will be sent to an
    ExecutionHandler.

    Handles the event of sending an Order to an execution system.
    The order contains a symbol (e.g. GOOG), a type (market or limit),
    quantity and a direction.
    """

    def __init__(self, symbol: str, order_type: OrderTypes, quantity: float,
                 direction: SignalTypes):
        """
        Initialises the order type, setting whether it is a Market order
        ('MKT') or Limit order ('LMT'), has a quantity (integral) and its
        direction ('BUY' or 'SELL').

        Parameters:
            symbol - The instrument to trade.
            order_type - 'MKT' or 'LMT' for Market or Limit.
            quantity - Non-negative integer for quantity.
            direction - 'BUY' or 'SELL' for long or short.
        """
        self.type = EventTypes.ORDER
        self.symbol = symbol
        self.order_type = order_type
        self.quantity = quantity
        self.direction = direction

    def __repr__(self):
        return f'Order: Symbol={self.symbol}, Type={self.order_type},' \
            f'Qnt={self.quantity}, Direction={self.direction}'


class FillEvent(Event):
    """
    When an ExecutionHandler receives an OrderEvent it must transact the order.
    Once an order has been transacted it generates a FillEvent, which describes
    the cost of purchase or sale as well as the transaction costs, such as fees
    or slippage.

    Encapsulates the notion of a Filled Order, as returned from a brokerage.
    Stores the quantity of an instrument actually filled and at what price.
    In addition, stores the commission of the trade from the brokerage.
    """

    def __init__(self, timeindex: str, symbol: str, exchange: str,
                 quantity: float, order_type: OrderTypes, direction: SignalTypes,
                 commission=None):
        """
        Initialises the FillEvent object. Sets the symbol, exchange,
        quantity, direction, cost of fill and an optional
        commission.

        If commission is not provided, the Fill object will
        calculate it based on the trade size and Interactive
        Brokers fees.

        Parameters:
            timeindex - The bar-resolution when the order was filled.
            symbol - The instrument which was filled.
            exchange - The exchange where the order was filled.
            quantity - The filled quantity.
            direction - The direction of fill ('BUY' or 'SELL')
            fill_cost - The holdings value in dollars.
            commission - An optional commission sent from IB.
        """
        self.type = EventTypes.FILL
        self.timeindex = timeindex
        self.symbol = symbol
        self.exchange = exchange
        self.quantity = quantity
        self.direction = direction
        # self.fill_cost = fill_cost
        self.order_type = order_type
        self.commission = commission or self.calculate_commision()

    def calculate_commision(self) -> float:
        """
        https://help.ftx.com/hc/en-us/articles/360024479432-Fees

        If order is maker - 0.02%
        If order is taker - 0.07%

        """
        commission = (0.07 / 100) * self.quantity
        if self.order_type == OrderTypes.MAKER:
            commission = (0.02 / 100) * self.quantity
        return commission
