from crypto_coin_factory import CoinFactoryExtended


def generate(currency):
    coin = CoinFactoryExtended().get_coin_service(currency).generate()
    print('Coin currency: ', currency)
    print("Coin address: ", coin.address)
    print("Coin wif: ", coin.wif)
    return coin


def test_gen_ada():
    coin = generate('ADA')
    assert coin.address is not None
    assert coin.wif is not None


def test_gen_bnb():
    coin = generate('BNB')
    assert coin.address is not None
    assert coin.wif is not None


def test_gen_bsv():
    coin = generate('BSV')
    assert coin.address is not None
    assert coin.wif is not None


def test_gen_club():
    coin = generate('CLUB')
    assert coin.address is not None
    assert coin.wif is not None


def test_gen_dash():
    coin = generate('DASH')
    assert coin.address is not None
    assert coin.wif is not None


def test_gen_eos():
    coin = generate('EOS')
    assert coin.address is not None
    assert coin.wif is not None


def test_gen_pote():
    coin = generate('POTE')
    assert coin.address is not None
    assert coin.wif is not None


def test_gen_xmr():
    coin = generate('XMR')
    assert coin.address is not None
    assert coin.wif is not None


def test_gen_xrp():
    coin = generate('XRP')
    assert coin.address is not None
    assert coin.wif is not None


def test_gen_d():
    coin = generate('D')
    assert coin.address is not None
    assert coin.wif is not None
