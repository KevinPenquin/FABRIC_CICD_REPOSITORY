# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

%pip install requests
%pip install yfinance

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import current_date

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import requests
import pandas as pd
from datetime import datetime

url = "https://query1.finance.yahoo.com/v7/finance/quote"

params = {
    "symbols": "ERW.BK,MINT.BK,CENTEL.BK,DUSIT.BK,^SET.BK"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, params=params, headers=headers)

data = response.json()



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import yfinance as yf

ticker = yf.Ticker("ERW.BK")
hist = ticker.history(period="1d", interval="5m")

hist

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import yfinance as yf

ticker = yf.Ticker("ERW.BK")

df = ticker.history(
    period="1d",
    interval="5m"
)

df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import yfinance as yf

tickers = ["ERW.BK", "MINT.BK", "CENTEL.BK", "DUSIT.BK", "^SET.BK"]

df = yf.download(
    tickers=tickers,
    period="1d",
    interval="5m",
    group_by="ticker",
    auto_adjust=True,
    progress=False
)

df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
