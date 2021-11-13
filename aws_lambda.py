import json

from keygen.crypto_coin_factory import CoinFactory


def lambda_handler(event, context):
    request_body = json.loads(event["body"])
    blockchain = request_body["blockchain"]
    quantity = request_body["quantity"]

    coin = blockchain.upper()
    factory = CoinFactory()
    crypto_keygen_service = factory.get_coin_service(coin)

    coins = crypto_keygen_service.generate_list(quantity)

    res = [{"wif": coin.wif, "address": coin.address, "snip": crypto_keygen_service.generate_asset_id(coin)} for coin in
           coins]

    body = json.dumps({
        'data': res,
        'metadata': {
            'blockchain': blockchain,
            'quantity': quantity
        }
    })

    return {
        'statusCode': 200,
        'body': body
    }
