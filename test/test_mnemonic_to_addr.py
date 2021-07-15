from plugins.d_crypto_coin_service import DenariusCoinService


def test_gen_coin_from_mnemonic_d0():
    coin = DenariusCoinService().generate_from_mnemonic('flock marble speed enjoy era chef ecology develop boost man stick glass')
    assert 'QSDoM1x6bu7BJH965SEu2GrGZdqXbjfBrjDYxfmfvkGYX7aCAPvX' == coin.wif
    assert 'DPNsvdVer4LPjPApt8hw4sFfwRfb7ihAHj' == coin.address

def test_gen_coin_from_mnemonic_d1():
    coin = DenariusCoinService().generate_from_mnemonic('salute equal wash will sister auto notable marble perfect private wrap park')
    assert 'QWHQY5iNj5HbS9M25yb2UVm8Lh8aqfJUuqbJ4NhkHQqLcczqL6Qd' == coin.wif
    assert 'DGkPXfipAat7QswFuZtDJ5CeNiPRQnpzDG' == coin.address