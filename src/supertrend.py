from src.atr import atr

"""
Tujuan:
- Menghitung indikator Supertrend.
- Indikator Supertrend membantu mengidentifikasi tren, menentukan level support dan resistance, dan menghasilkan sinyal beli dan jual.

Parameter:
- df: DataFrame yang berisi data harga dengan kolom 'high', 'low', dan 'close'.
- period: (int, optional) Periode untuk perhitungan Average True Range (ATR). Defaultnya adalah 7.
- atr_multiplier: (float, optional) Pengali yang digunakan untuk ATR dalam menghitung upper dan lower band. Defaultnya adalah 3.

Returns:
- DataFrame yang sama dengan input, dengan kolom tambahan:
    - atr: Nilai Average True Range (ATR) untuk setiap periode.
    - upperband: Upper band dari indikator Supertrend.
    - lowerband: Lower band dari indikator Supertrend.
    - is_uptrend: Boolean flag yang menunjukkan apakah tren saat ini adalah uptrend (True) atau downtrend (False).

How to work:
1. Menghitung nilai True Range (TR) menggunakan fungsi atr().
2. Menghitung nilai rata-rata TR (ATR) untuk periode yang ditentukan.
3. Menghitung upper dan lower band dengan menambahkan dan mengurangi ATR yang dikalikan dengan atr_multiplier dari nilai rata-rata antara harga tertinggi dan terendah (hl_2).
4. Menginisialisasi kolom is_uptrend dengan nilai True.
5. Mengiterasi setiap baris DataFrame, mulai dari baris kedua:
    - Jika harga penutupan saat ini di atas upper band sebelumnya, maka tren saat ini adalah uptrend.
    - Jika harga penutupan saat ini di bawah lower band sebelumnya, maka tren saat ini adalah downtrend.
    - Jika harga penutupan berada di antara upper dan lower band, maka tren tetap sama dengan tren sebelumnya.
    - Memperbarui nilai upper dan lower band jika perlu untuk mempertahankan tren yang sedang berlangsung.
"""


def supertrend(df, period=7, atr_multiplier=3):
    hl_2 = (df["high"] + df["low"]) / 2
    df["atr"] = atr(df, period)
    df["upperband"] = hl_2 + (atr_multiplier * df["atr"])
    df["lowerband"] = hl_2 - (atr_multiplier * df["atr"])
    df["is_uptrend"] = True

    for curr in range(1, len(df.index)):
        prev = curr - 1

        if df["close"][curr] > df["upperband"][prev]:
            df["is_uptrend"] = True
        elif df["close"][curr] < df["lowerband"][prev]:
            df["is_uptrend"] = False
        else:
            df["is_uptrend"][curr] = df["is_uptrend"][prev]

            if df['is_uptrend'][curr] and df['lowerband'][curr] < df['lowerband'][prev]:
                df['lowerband'][curr] = df['lowerband'][prev]

            if not df['is_uptrend'][curr] and df['upperband'][curr] > df['upperband'][prev]:
                df['upperband'][curr] = df['upperband'][prev]
    
    return df
        