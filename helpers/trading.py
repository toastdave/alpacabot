import os

from dotenv import load_dotenv
from alpaca.trading.client import TradingClient


load_dotenv()

trading_client = TradingClient(os.ALPACA_API_KEY, os.ALPACA_API_SECRET, paper=True)