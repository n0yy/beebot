def tr(data):
    """
        True Range (TR) adalah indikator volatilitas yang mengukur rentang harga yang ditempuh oleh sebuah aset selama periode tertentu. Nilai TR yang tinggi menunjukkan volatilitas yang tinggi, sedangkan nilai TR yang rendah menunjukkan volatilitas yang rendah.
    """
    data["prev_close"] = data["close"].shift(1)
    data["high-low"] = abs(data["high"] - data["low"])
    data["high-pc"] = abs(data["high"] - data["prev_close"])
    data["low-pc"] = abs(data["low"] - data["prev_close"])

    tr = data[["high-low", "high-pc", "low-pc"]].max(axis=1)
    return tr