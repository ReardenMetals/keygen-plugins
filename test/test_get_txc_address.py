from plugins.txc_crypto_coin_service import TexitCoinCoinService, TexitCoinConf


def test_get_address_txc0():
    address = TexitCoinCoinService().get_address('VgAD16hCTgrvsWZLJygPzrhKvYcd4x1Ug8pHUvGqVUn2ZU8P6bBA')
    assert 'txc1qq6dwyy99xptw3hy07jl38dcmlkq93urvd6yqp5' == address

def test_get_address_txc1():
    address = TexitCoinCoinService().get_address('Vad1DZkaZ6mUTB1LoLtQzL3V24yj442nTmP6xHAW98HSKPPnbTno')
    assert 'txc1q6nkm2zv44udzpsh80x7mv6rk7tmyfj39fuvr8d' == address

def test_get_address_txc1_1():
    address = TexitCoinCoinService().get_address('Vc6c4MVptDdyb5vH9H6rsB4Gg3E4Y5RVY32L8VuY2UXXs8CC5KJe')
    assert 'txc1q6nkm2zv44udzpsh80x7mv6rk7tmyfj39fuvr8d' == address


def test_get_address_txc2():
    address = TexitCoinCoinService().get_address('VeELq173c2vR2ZmSeTsjtr8DJuCZ4dmk1GWxX3U5MxvyCDvZrFey')
    print(address)
    assert 'txc1q8mg97jfx3vzxr8rnm5xzf7lxmp475x4eaw0m4u' == address

def test_gen_coin_txc0():

    coin = TexitCoinCoinService().generate()
    print(coin)




    # assert 'QSDoM1x6bu7BJH965SEu2GrGZdqXbjfBrjDYxfmfvkGYX7aCAPvX' == coin.wif
    # assert 'DPNsvdVer4LPjPApt8hw4sFfwRfb7ihAHj' == coin.address

# def test_gen_coin_from_mnemonic_d1():
#     coin = TexitCoinCoinService().generate_from_mnemonic('salute equal wash will sister auto notable marble perfect private wrap park')
#     assert 'QWHQY5iNj5HbS9M25yb2UVm8Lh8aqfJUuqbJ4NhkHQqLcczqL6Qd' == coin.wif
#     assert 'DGkPXfipAat7QswFuZtDJ5CeNiPRQnpzDG' == coin.address