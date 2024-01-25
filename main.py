from src.exchange.binance import Binance

import schedule
import pandas as pd
pd.set_option("display.max_rows", None)

import warnings
warnings.filterwarnings("ignore")

import numpy as np
from datetime import datetime
import time

# INSTANCE EXCHANGE
binance = Binance()
binance.get_spot_balance()