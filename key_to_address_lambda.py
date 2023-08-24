import json

from keygen.crypto_coin_factory import CoinFactory


def lambda_handler(event, context):
    request_body = json.loads(event["body"])
    blockchain = request_body["blockchain"]
    private_key = request_body["privateKey"]

    coin = blockchain.upper()
    factory = CoinFactory()
    crypto_keygen_service = factory.get_coin_service(coin)

    address = crypto_keygen_service.get_address(private_key)

    body = json.dumps({
        'address': address,
        'blockchain': blockchain,
        'privateKey': private_key
    })

    return {
        'statusCode': 200,
        'body': body
    }
