from key_to_address_lambda import lambda_handler
import json


def test_key_to_lambda_blockchain_defined():
    event = {"body": json.dumps(
        {"blockchain": "tBTC", "privateKey": "cW418jets2Prj6wGsmN1aCLUuQFJuPWmnoiETmw8kNzuAGnhKcw6"})}

    response = lambda_handler(event, None)

    print(response)


def test_key_to_lambda_blockchain_not_defined():
    event = {"body": json.dumps({"privateKey": "cW418jets2Prj6wGsmN1aCLUuQFJuPWmnoiETmw8kNzuAGnhKcw6"})}

    response = lambda_handler(event, None)

    print(response)
