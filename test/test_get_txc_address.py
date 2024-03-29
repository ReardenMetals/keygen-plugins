from plugins.txc_crypto_coin_service import TexitCoinCoinService, TexitCoinConf


def test_get_address_txc0():
    address = TexitCoinCoinService().get_address('VgEB4hJvq4HZPrRbTtGHjW25UijkeJEkdryiEnfCbf9LfLEjzdyK')
    assert 'TjMPrSpiEuwxuKCoELHUCp7hvfBprtk8uf' == address

def test_get_address_txc0():
    address = TexitCoinCoinService().get_address('VejDLJxncb2GBr4jVaQESFcQiUDGLTiYAm6pHhRY5mmwNZ3wq2bQ')
    assert 'TdKREogjUYxADbFioWAD2CA611GMyyzBWM' == address



def test_get_address_txc1():
    address = TexitCoinCoinService().get_address('Vh7hXRrTwTc6Ps5ntf4aRD7iH31oxxyygBVo2zVxzX3MJrNdgYJv')
    print(address)
    assert 'Thv4aQnFrxZELdV2sbzr6GcqnFgmErpB8Y' == address

def test_gen_coin_txc0():

    coin = TexitCoinCoinService().generate()
    print(coin)




    # assert 'QSDoM1x6bu7BJH965SEu2GrGZdqXbjfBrjDYxfmfvkGYX7aCAPvX' == coin.wif
    # assert 'DPNsvdVer4LPjPApt8hw4sFfwRfb7ihAHj' == coin.address

# def test_gen_coin_from_mnemonic_d1():
#     coin = TexitCoinCoinService().generate_from_mnemonic('salute equal wash will sister auto notable marble perfect private wrap park')
#     assert 'QWHQY5iNj5HbS9M25yb2UVm8Lh8aqfJUuqbJ4NhkHQqLcczqL6Qd' == coin.wif
#     assert 'DGkPXfipAat7QswFuZtDJ5CeNiPRQnpzDG' == coin.address