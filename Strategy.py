import pandas as pd
import pandas_ta as ta

def analyze(df):
    df.ta.ema(length=20, append=True)
    df.ta.ema(length=50, append=True)
    df.ta.rsi(length=14, append=True)
    df.ta.macd(append=True)

    last = df.iloc[-1]
    prev = df.iloc[-2]

    ema20 = last["EMA_20"]
    ema50 = last["EMA_50"]
    rsi = last["RSI_14"]
    macd = last["MACD_12_26_9"]
    signal = last["MACDs_12_26_9"]

    if ema20 > ema50 and rsi > 50 and macd > signal:
        return "BUY"
    elif ema20 < ema50 and rsi < 50 and macd < signal:
        return "SELL"
    return None
