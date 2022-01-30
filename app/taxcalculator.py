from app import app, pricefetcher, accountreader
import constants


@app.route("/getAccountTransactionsByYear/<account>/<year>")
def calculateTransactionAmount(year, account):
    transactions = accountreader.getTransactionDetails(account).json()
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


@app.route("/getAccountIncomeByYear/<account>/<year>")
def calculateAccountIncome(year, account):
    usdTrxPrices = calculateTransactionAmount(year, account)
    total = 0.0
    for price in usdTrxPrices:
        total += price
    return str(total)
