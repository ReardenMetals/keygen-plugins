from keygen.currencies.ltc_crypto_coin_service import LtcCoinService
from plugins.txc_crypto_coin_service import TexitCoinCoinService


# def test_get_address_d0():
#     address = TexitCoinCoinService().get_address('QSDoM1x6bu7BJH965SEu2GrGZdqXbjfBrjDYxfmfvkGYX7aCAPvX')
#     assert 'DPNsvdVer4LPjPApt8hw4sFfwRfb7ihAHj' == address


# def test_get_address_d1():
#     address = TexitCoinCoinService().get_address('QWHQY5iNj5HbS9M25yb2UVm8Lh8aqfJUuqbJ4NhkHQqLcczqL6Qd')
#     assert 'DGkPXfipAat7QswFuZtDJ5CeNiPRQnpzDG' == address

def test_gen_coin_ltc0():
    coin = LtcCoinService().generate()
    print(coin)

def test_gen_coin_txc0():

    coin = TexitCoinCoinService().generate()
    print(coin)


    # assert 'QSDoM1x6bu7BJH965SEu2GrGZdqXbjfBrjDYxfmfvkGYX7aCAPvX' == coin.wif
    # assert 'DPNsvdVer4LPjPApt8hw4sFfwRfb7ihAHj' == coin.address

# def test_gen_coin_from_mnemonic_d1():
#     coin = TexitCoinCoinService().generate_from_mnemonic('salute equal wash will sister auto notable marble perfect private wrap park')
#     assert 'QWHQY5iNj5HbS9M25yb2UVm8Lh8aqfJUuqbJ4NhkHQqLcczqL6Qd' == coin.wif
#     assert 'DGkPXfipAat7QswFuZtDJ5CeNiPRQnpzDG' == coin.address