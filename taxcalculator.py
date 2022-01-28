import datetime
import pricefetcher
import accountreader
import constants

prices = pricefetcher.getEthPrices(2021)
# print(prices.json())

transactions = accountreader.getTransactionDetails(None).json()
# for trx in transactions["result"]:
#     if trx["to"] == constants.MY_PUBLIC_ADDRESS:
#         print(trx)

for trx in transactions["result"]:
    if trx["to"] == constants.MY_PUBLIC_ADDRESS:
        currentTime = int(trx["timeStamp"])
        minusTwentyFour = currentTime - (24 * 60 * 60)
        matchingPrice = any(
            int(price[0]) <= currentTime and int(price[0]) >= minusTwentyFour
            for price in prices
        )
        print(matchingPrice)
