import requests

api = "https://api.cryptowat.ch/markets/kraken/ethusd/ohlc?after=1609459200&before=1640995199&periods=86400"
response = requests.get(api)

response.json()
