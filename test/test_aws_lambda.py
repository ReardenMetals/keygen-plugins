import json

from aws_lambda import lambda_handler
from crypto_coin_factory import CoinFactoryExtended


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
    fetched_address = CoinFactoryExtended().get_coin_service('BTC').get_address(private_key=wif)
    assert address == fetched_address
