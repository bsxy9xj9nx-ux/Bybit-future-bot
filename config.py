import os
from dotenv import load_dotenv

load_dotenv()

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
INTERVAL = "15"
LEVERAGE = 10
RISK_PERCENT = 1.0
