from plugins.ada_crypto_coin_service import CardanoCoinService

ada_crypto_coin_service = CardanoCoinService()


def test_generate():
    coin = ada_crypto_coin_service.generate()
    print()
    print("Coin address: ", coin.address)
    print("Coin wif: ", coin.wif)
    print("Coin seed: ", coin.seed)
    print("Coin asset ID: ", ada_crypto_coin_service.generate_asset_id(coin))

    assert coin.address is not None
    assert coin.wif is not None


def test_get_coin():
    mnemonic = "join sketch kick viable culture diamond search wheel half tissue quote juice veteran sand hub"
    coin = ada_crypto_coin_service.get_coin(mnemonic)
    print()
    print("Coin address: ", coin.address)
    print("Coin wif: ", coin.wif)
    print("Coin seed: ", coin.seed)
    print("Coin asset ID: ", ada_crypto_coin_service.generate_asset_id(coin))

    expected_address = "addr1qx08qw2e9vhqm708znk3xdeg5x7ptf80uqs8cjlxaqkgdrxhzz8m7cj5wfhgakp5hcea6nqmdze6323luye7v23ze8gsv48609"
    assert coin.address is not None
    assert coin.address == expected_address
    assert coin.wif is not None