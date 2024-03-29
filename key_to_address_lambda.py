import json

from keygen.crypto_coin_factory import CoinFactory


def lambda_handler(event, context):
    request_body = json.loads(event["body"])

    blockchain = None
    if 'blockchain' in request_body:
        blockchain = request_body["blockchain"]

    private_key = request_body["privateKey"]

    returned_result = {"coin": None, "coin_candidates": []}
    address = None
    if blockchain:
        crypto_keygen_service = CoinFactory().get_coin_service(blockchain)
        address = crypto_keygen_service.get_address(private_key)
        returned_result["coin"] = {
            'address': address,
            'blockchain': blockchain,
            'privateKey': private_key
        }

    coin_candidates = []
    currencies = CoinFactory().get_available_currencies()
    for currency in currencies:
        try:
            address = CoinFactory().get_coin_service(currency).get_address(private_key)
        except:
            pass  # Exception loading address by private key for currency
        if address:
            coin_candidates.append(
                {
                    'address': address,
                    'blockchain': currency,
                    'privateKey': private_key
                }
            )
    returned_result["coin_candidates"] = coin_candidates

    return {
        'statusCode': 200,
        'body': json.dumps(returned_result)
    }
