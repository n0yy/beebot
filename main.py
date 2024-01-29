from src.exchange.binance import Binance
from src.Bot import BeeBot

import schedule
import pandas as pd
pd.set_option("display.max_rows", None)

import warnings
warnings.filterwarnings("ignore")

import time

# INSTANCE EXCHANGE
binance = Binance()
binance.get_spot_balance()

# INSTANCE BOT
# quantity = 0.0006 / +- Rp 21.000
bot = BeeBot(binance.exchange, "ETH/BIDR", quantity=0.0006)

def run_bot():
    bot.run()

schedule.every(10).seconds.do(run_bot)
while True:
    schedule.run_pending()
    time.sleep(1)