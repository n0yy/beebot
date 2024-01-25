import ccxt
from decouple import config
import pandas as pd

class Binance:
    def __init__(self):
        self.exchange = ccxt.binance({
            "apiKey": config("BINANCE_API_KEY"),
            "secret": config("BINANCE_SECRET_KEY")
        })

        self.profile = pd.DataFrame.from_dict(self.exchange.fetch_balance())

    def get_spot_balance(self):
        asset = self.profile["info"][13]
        asset = pd.DataFrame(asset)
        # change type
        asset["free"] = asset["free"].astype("float")
        # drop column locked
        asset.drop(columns=["locked"], inplace=True)
        
        print("=========== SPOT BALANCE ===========")
        # get crypto balance when not 0
        print(asset[(asset["free"] > 0)])
