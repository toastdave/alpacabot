import os

from dotenv import load_dotenv
from alpaca.data import StockHistoricalDataClient, CryptoHistoricalDataClient, OptionHistoricalDataClient

load_dotenv()

stock_client = StockHistoricalDataClient(os.ALPACA_API_KEY, os.ALPACA_API_SECRET)