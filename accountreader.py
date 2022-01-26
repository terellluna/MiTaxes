import requests
import constants

etherscanAPI = "https://api.etherscan.io/api"

blockPayload = {
    "module": "account",
    "action": "getminedblocks",
    "address": constants.MY_PUBLIC_ADDRESS,
    "blocktype": "blocks",
    "page": 1,
    "offset": 50,
    "apikey": constants.API_KEY_ETHERSCAN,
}

transactionPayload = {
    "module": "account",
    "action": "txlist",
    "address": constants.MY_PUBLIC_ADDRESS,
    "startblock": 0,
    "endblock": 99999999,
    "page": 1,
    "offset": 50,
    "sort": "asc",
    "apikey": constants.API_KEY_ETHERSCAN,
}

transactionResponse = requests.get(etherscanAPI, params=transactionPayload)

for trx in transactionResponse.json()["result"]:
    if trx["to"] == constants.MY_PUBLIC_ADDRESS:
        print(trx)

# print(transactionResponse.json())
