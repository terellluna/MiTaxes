import requests
import datetime
import constants


def getEthPrices(year):
    aftertime = datetime.datetime(int(year), 1, 1, 0, 0, 0).timestamp()
    beforetime = datetime.datetime(int(year), 12, 31, 11, 59, 59).timestamp()
    payload = {"before": int(beforetime), "after": int(aftertime), "periods": 86400}
    response = requests.get(constants.PRICE_API_ETHUSD, params=payload)
    return response


def getErgPrices(year):
    aftertime = datetime.datetime(int(year), 1, 1, 0, 0, 0).timestamp()
    beforetime = datetime.datetime(int(year), 12, 31, 11, 59, 59).timestamp()
    payload = {"before": int(beforetime), "after": int(aftertime), "periods": 86400}
    response = requests.get(constants.PRICE_API_ERGUSDT, params=payload)
    return response
