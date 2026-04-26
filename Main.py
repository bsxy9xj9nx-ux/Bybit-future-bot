import asyncio
import pandas as pd
from pybit.unified_trading import HTTP
from config import BYBIT_API_KEY, BYBIT_API_SECRET, SYMBOLS, INTERVAL, LEVERAGE, RISK_PERCENT
from strategy import analyze
from bot import send_message

client = HTTP(api_key=BYBIT_API_KEY, api_secret=BYBIT_API_SECRET)

def get_klines(symbol):
    resp = client.get_kline(category="linear", symbol=symbol, interval=INTERVAL, limit=100)
    data = resp["result"]["list"]
    df = pd.DataFrame(data, columns=["time","open","high","low","close","volume","turnover"])
    df = df.astype(float)
    df = df.iloc[::-1].reset_index(drop=True)
    return df

def get_balance():
    resp = client.get_wallet_balance(accountType="UNIFIED")
    return float(resp["result"]["list"][0]["totalEquity"])

def place_order(symbol, side):
    balance = get_balance()
    price = float(client.get_tickers(category="linear", symbol=symbol)["result"]["list"][0]["lastPrice"])
    qty = round((balance * RISK_PERCENT / 100) * LEVERAGE / price, 3)
    client.set_leverage(category="linear", symbol=symbol, buyLeverage=str(LEVERAGE), sellLeverage=str(LEVERAGE))
    client.place_order(category="linear", symbol=symbol, side=side, orderType="Market", qty=str(qty))

async def main():
    while True:
        for symbol in SYMBOLS:
            try:
                df = get_klines(symbol)
                signal = analyze(df)
                if signal:
                    place_order(symbol, signal)
                    await send_message(f"✅ {symbol} — {signal}")
            except Exception as e:
                await send_message(f"❌ Ошибка {symbol}: {e}")
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
