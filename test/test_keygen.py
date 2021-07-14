from crypto_coin_factory import CoinFactoryExtended


def generate(currency):
    coin = CoinFactoryExtended().get_coin_service(currency).generate()
    print('Coin currency: ', currency)
    print("Coin address: ", coin.address)
    print("Coin wif: ", coin.wif)
    return coin


def test_gen_btc():
    coin = generate('D')
    assert coin.address is not None
    assert coin.wif is not None


