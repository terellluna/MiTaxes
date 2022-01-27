import pricefetcher
import accountreader
import constants

prices = pricefetcher.getEthPrices(2021)
# print(prices.json())

accountData = accountreader.getAccountDetails(None)
for trx in accountData.json()["result"]:
    if trx["to"] == constants.MY_PUBLIC_ADDRESS:
        print(trx)
