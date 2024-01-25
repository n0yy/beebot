from src.tr import tr

def atr(data, period):
    data["tr"] = tr(data)
    atr = data["tr"].rolling(period).mean()
    return atr