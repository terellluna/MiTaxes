import requests
import datetime

# get user tax year
year = input("Enter the year for which you wish to calculate your tax liability: ")

# after time is the beginning of the year
aftertime = datetime.datetime(int(year), 1, 1, 0, 0, 0).timestamp()

# before time is the end of the year
beforetime = datetime.datetime(int(year), 12, 31, 11, 59, 59).timestamp()

# set the payload using the aftertime, beforetime, and the period (day)
payload = {"before": int(beforetime), "after": int(aftertime), "periods": 86400}

# api url
priceAPI = "https://api.cryptowat.ch/markets/kraken/ethusd/ohlc"

# request call and response capture
response = requests.get(priceAPI, params=payload)

# display price data
response.json()

print(response.json())
