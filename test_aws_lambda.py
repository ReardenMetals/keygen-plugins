import json

from aws_lambda import lambda_handler
from keygen.crypto_coin_factory import CoinFactory


def test_aws_lambda_keygen():
    event = {"body": "{\"blockchain\":\"BTC\", \"quantity\": 10}"}
    res = lambda_handler(event=event, context=None)
    body = res['body']
    body_json = json.loads(body)
    data = body_json['data']
    assert len(data) == 10
    coin = data[0]
    wif = coin['wif']
    address = coin['address']
    fetched_address = CoinFactory().get_coin_service('BTC').get_address(private_key=wif)
    assert address == fetched_address


def test_aws_lambda_keygen_ada():
    event = {"body": "{\"blockchain\":\"ADA\", \"quantity\": 10}"}
    res = lambda_handler(event=event, context=None)
    body = res['body']
    body_json = json.loads(body)
    data = body_json['data']
    assert len(data) == 10
    coin = data[0]
    wif = coin['wif']
    address = coin['address']
    fetched_address = CoinFactory().get_coin_service('ADA').get_address(private_key=wif)
    assert address == fetched_address


def main():
    test_aws_lambda_keygen()
    test_aws_lambda_keygen_ada()
    print("Success!")


if __name__ == '__main__':
    main()
