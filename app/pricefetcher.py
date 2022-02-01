import requests
import datetime
import constants


def getEthPrices(year):
    aftertime = datetime.datetime(int(year), 1, 1, 0, 0, 0).timestamp()
    beforetime = datetime.datetime(int(year), 12, 31, 11, 59, 59).timestamp()
    payload = {"before": int(beforetime), "after": int(aftertime), "periods": 86400}
    priceAPI = "https://api.cryptowat.ch/markets/kraken/ethusd/ohlc"
    response = requests.get(priceAPI, params=payload)
    return response
