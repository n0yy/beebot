import pandas as pd
from datetime import datetime
from src.supertrend import supertrend

class BeeBot:
    def __init__(self, exchange, symbol:str, quantity:float):
        self.in_position = False
        self.exchange = exchange
        self.symbol = symbol
        self.quantity = quantity

    def check_signals(self, df):

        print("Checking Buy/Sell Signals")
        print(df.tail(5))
        last_row_index = len(df.index) - 1
        previous_row_index = last_row_index - 1

        if not df['is_uptrend'][previous_row_index] and df['is_uptrend'][last_row_index]:
            print("Changed to Uptrend, BUY IT!")
            if not self.in_position:
                order = self.exchange.create_market_buy_order(self.symbol, self.quantity)
                print(order)
                self.in_position = True
            else:
                print("Already in position, nothing to do")
        
        if df['is_uptrend'][previous_row_index] and not df['is_uptrend'][last_row_index]:
            if self.in_position:
                print("Changed to Downtrend, SELL IT!")
                order = self.exchange.create_market_sell_order(self.symbol, self.quantity)
                print(order)
                self.in_position = False
            else:
                print("You aren't in position, nothing to sell")

    def run(self):
        print(f"Fetching new bars for {datetime.now().isoformat()}")
        bars = self.exchange.fetch_ohlcv(self.symbol, timeframe='1m', limit=200)
        df = pd.DataFrame(bars[:-1], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

        st = supertrend(df)
        
        self.check_signals(st)