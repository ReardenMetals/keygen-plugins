from crypto_coin_factory import CoinFactoryExtended


def get_coin_address(currency, private_key):
    service = CoinFactoryExtended().get_coin_service(currency)
    return service.get_address(private_key)


def test_get_address_ada():
    address = get_coin_address('ADA', 'tilt occur nature trend drip catalog clinic settle vague spin yellow differ')
    assert 'Ae2tdPwUPEZ76ux7XNfaTuRwoXqnyWYmVzxEDa4NFDqvJcknhhAVr1um7N6' == address


def test_get_address_bnb():
    address = get_coin_address('BNB', 'de593950406e0722dce708d6cb2af5fbc40ab699cd1835a9789b20d792038dd2')
    assert 'bnb1tfwk5rpcku8u3e6c7ud8p0dzju5ek5pc3zlfgw' == address


def test_get_address_bsv():
    address = get_coin_address('BSV', 'KyrsMv94pbbHJcnFJ4S73mqL6EaK2xzzLHGz6399qpmF96q7etox')
    assert '1BquZU6ZUSphuGaNfPX8GMkNpg6hF1TAiB' == address


def test_get_address_club():
    address = get_coin_address('CLUB', 'Ph9cfu3b43TGtu3KP1Qypjf7qk9g6R5Pi6Z9aC3prw6PGNfeWd7h')
    assert 'CbXLCWrCqET3Z3XzWAuaLVzPVe2bUpWNbS' == address


def test_get_address_dash():
    address = get_coin_address('DASH', 'XEjo8DrV4kD8jMXLGRTGqdpY3Twickx8Tgph7kP4RWJMZPCt9PZj')
    assert 'XbiEFxMMUXX5pn4ei143ayD2inkiaTgG3f' == address


def test_get_address_eos():
    address = get_coin_address('EOS', '5KE27gypNyCscnNUWfSxyRYicw7Q7TZWSyQvVFWDSpktmqMdAcY')
    assert 'EOS6F72yxg33HyVcgmFCdn9ozjvaQDHqkANRwKW5h8qY1S4acpTaa' == address


def test_get_address_pote():
    address = get_coin_address('POTE', 'U9TJmqAzPTBZRcBj1wcDxkbZP5PFohWcpvumXzkvxeHtoLugo8TW')
    assert 'PS1uC735ZrJXreEomy3BzMvnmjJGqyCpMR' == address


def test_get_address_xmr():
    address = get_coin_address('XMR',
                               'phone moisture natural makeup mayor thorn hold luxury below abort evicted inwardly '
                               'urchins reorder frying gills drinks acoustic swung kernels across suddenly vexed dogs '
                               'vexed')
    assert '41puPXghUHQM8SAK9cErNXb8z98h6q1pAXJh5Le2SscTYXMDzqdw5cBXKtF3VgvG8EGwzxrwejFsnWNc6xLkM9zPLjqTYuh' == address


def test_get_address_xrp():
    address = get_coin_address('XRP', '069ce4e08b502ac1d87cd843c1fc8bdd518da4088c4226219f8c2eeabaf0ac1f')
    assert 'rUH8TjU6SGe2NEqX8qRfanRU6MBQjbDkeZ' == address


def test_get_address_d0():
    address = get_coin_address('D', 'QSDoM1x6bu7BJH965SEu2GrGZdqXbjfBrjDYxfmfvkGYX7aCAPvX')
    assert 'DPNsvdVer4LPjPApt8hw4sFfwRfb7ihAHj' == address


def test_get_address_d1():
    address = get_coin_address('D', 'QWHQY5iNj5HbS9M25yb2UVm8Lh8aqfJUuqbJ4NhkHQqLcczqL6Qd')
    assert 'DGkPXfipAat7QswFuZtDJ5CeNiPRQnpzDG' == address

