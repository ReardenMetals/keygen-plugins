from crypto_coin_factory import CoinFactoryExtended


def get_coin_address(currency, private_key):
    service = CoinFactoryExtended().get_coin_service(currency)
    return service.get_address(private_key)


def test_get_address_d0():
    address = get_coin_address('D', 'QSDoM1x6bu7BJH965SEu2GrGZdqXbjfBrjDYxfmfvkGYX7aCAPvX')
    assert 'DPNsvdVer4LPjPApt8hw4sFfwRfb7ihAHj' == address


def test_get_address_d1():
    address = get_coin_address('D', 'QWHQY5iNj5HbS9M25yb2UVm8Lh8aqfJUuqbJ4NhkHQqLcczqL6Qd')
    assert 'DGkPXfipAat7QswFuZtDJ5CeNiPRQnpzDG' == address
