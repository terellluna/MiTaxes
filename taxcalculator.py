import datetime
import pricefetcher
import accountreader
import constants


def calculateTransactionAmount(transactions, prices):
    usdTrxPrices = []
    for trx in transactions["result"]:
        if trx["to"] == constants.MY_PUBLIC_ADDRESS:
            currentTime = int(trx["timeStamp"])
            minusTwentyFour = currentTime - (24 * 60 * 60)
            for price in prices:
                if int(price[0]) <= currentTime and int(price[0]) >= minusTwentyFour:
                    trxAmount = float(trx["value"]) / 1000000000000000000
                    usdPrice = price[4]
                    usdTrxPrices.append(trxAmount * usdPrice)
    return usdTrxPrices


def calculateAccountIncome(usdTrxPrices):
    total = 0.0
    for price in usdTrxPrices:
        total += price
    return total


prices = pricefetcher.getEthPrices(2021).json()["result"]["86400"]
# print(prices)
# for price in prices:
#     print(price)

transactions = accountreader.getTransactionDetails(None).json()
# for trx in transactions["result"]:
#     if trx["to"] == constants.MY_PUBLIC_ADDRESS:
#         print(trx)
usdTrxPrices = calculateTransactionAmount(transactions, prices)

print(f"Total Transaction Income: {calculateAccountIncome(usdTrxPrices)}")
