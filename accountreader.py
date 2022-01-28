import requests
import constants


def getTransactionDetails(publicAddress=constants.MY_PUBLIC_ADDRESS):
    TRANSACTION_PAYLOAD = {
        "module": "account",
        "action": "txlist",
        "address": publicAddress,
        "startblock": 0,
        "endblock": 99999999,
        "page": 1,
        "offset": 50,
        "sort": "asc",
        "apikey": constants.API_KEY_ETHERSCAN,
    }

    return requests.get(constants.ETHERSCAN_API, params=constants.TRANSACTION_PAYLOAD)
