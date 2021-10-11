import queue

from .data import DataHandler
from .strategy import Strategy
from .portfolio import Portfolio
from .execution import ExecutionHandler

from .enums import EventTypes


def backtest(events: queue.Queue(), bars: DataHandler, strategy: Strategy,
             portfolio: Portfolio, broker: ExecutionHandler) -> None:

    while True:
        # Update the bars (specific backtest code, as opposed to live trading)
        if bars.continue_backtest == True:
            bars.update_bars()
        else:
            break

        # Handle the events
        while True:
            try:
                event = events.get(False)

                if event is not None:
                    if event.type == EventTypes.MARKET:
                        strategy.calculate_signals(event)
                        portfolio.update_timeindex(event)

                    elif event.type == EventTypes.SIGNAL:
                        portfolio.update_signal(event)

                    elif event.type == EventTypes.ORDER:
                        broker.execute_order(event)

                    elif event.type == EventTypes.FILL:
                        portfolio.update_fill(event)

            except queue.Empty:
                break
