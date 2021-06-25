from plugins.ada_crypto_coin_service import CardanoCoinService
from plugins.bnb_crypto_coin_service import BnbCoinService
from plugins.bsv_crypto_coin_service import BsvCoinService
from plugins.eos_crypto_coin_service import EosCoinService
from plugins.xmr_crypto_coin_service import XmrCoinService


def test_bnb_gen():
    service = BnbCoinService()
    coin = service.generate()
    print(coin)

def test_eos_gen():
    service = EosCoinService()
    coin = service.generate()
    print(coin)

def test_xmr_gen():
    service = XmrCoinService()
    coin = service.generate()
    print(coin)

def test_ada_gen():
    service = CardanoCoinService()
    coin = service.generate()
    print(coin)

def test_bsv_gen():
    service = BsvCoinService()
    coin = service.generate()
    wif = coin.wif
    print(coin)
    cc = service.get_coin(wif)
    print(cc)

def main():
    print("Hello world")
    test_ada_gen()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# Needed dependenices: XMR, WAVES, USDT, EOS, BSV, ADA