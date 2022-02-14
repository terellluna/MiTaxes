from unittest.main import MAIN_EXAMPLES
from app import app, pricefetcher, accountreader
import constants


@app.route("/getAccountTransactionsByYearEth/<account>/<year>")
def calculateTransactionAmountEth(year, account):
    transactions = accountreader.getTransactionDetailsEth(account).json()
    prices = pricefetcher.getEthPrices(year).json()["result"]["86400"]
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


@app.route("/getAccountTransactionsByYearErg/<account>/<year>")
def calculateTransactionAmountErg(year, account):
    transactions = accountreader.getTransactionDetailsErg(account).json()
    prices = pricefetcher.getErgPrices(year).json()["result"]["86400"]
    usdTrxPrices = []
    for item in transactions["items"]:
        for output in item["outputs"]:
            if output["address"] == constants.MY_PUBLIC_ADDRESS_ERG:
                currentTime = int(item["timestamp"]) / 1000
                minusTwentyFour = currentTime - (24 * 60 * 60)
                for price in prices:
                    if (
                        int(price[0]) <= currentTime
                        and int(price[0]) >= minusTwentyFour
                    ):
                        trxAmount = float(output["value"]) / 1000000000
                        usdPrice = price[4]
                        usdTrxPrices.append(trxAmount * usdPrice)
    return usdTrxPrices


@app.route("/getAccountIncomeByYearEth/<account>/<year>")
def calculateAccountIncomeEth(year, account):
    usdTrxPrices = calculateTransactionAmountEth(year, account)
    total = 0.0
    for price in usdTrxPrices:
        total += price
    return str(total)


@app.route("/getAccountIncomeByYearErg/<account>/<year>")
def calculateAccountIncomeErg(year, account):
    usdTrxPrices = calculateTransactionAmountErg(year, account)
    total = 0.0
    for price in usdTrxPrices:
        total += price
    return str(total)
