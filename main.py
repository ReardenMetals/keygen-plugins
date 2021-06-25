from plugins.bnb_crypto_coin_service import BnbCoinService
from plugins.bsv_crypto_coin_service import BsvCoinService
from plugins.club_crypto_coin_service import ClubCoinService
from plugins.dash_crypto_coin_service import DashCoinService
from plugins.eos_crypto_coin_service import EosCoinService
from plugins.pote_crypto_coin_service import PoteCoinService
from plugins.xmr_crypto_coin_service import XmrCoinService
from plugins.xrp_crypto_coin_service import RippleCoinService
from plugins.ada_crypto_coin_service import CardanoCoinService

def test_ada_gen():
    service = CardanoCoinService()
    coin = service.generate()
    print(coin)

def test_bnb_gen():
    service = BnbCoinService()
    coin = service.generate()
    print(coin)

def test_bsv_gen():
    service = BsvCoinService()
    coin = service.generate()
    wif = coin.wif
    print(coin)
    # cc = service.get_coin(wif)
    # print(cc)

def test_club_gen():
    service = ClubCoinService()
    coin = service.generate()
    print(coin)

def test_dash_gen():
    service = DashCoinService()
    coin = service.generate()
    print(coin)

def test_eos_gen():
    service = EosCoinService()
    coin = service.generate()
    print(coin)

def test_pote_gen():
    service = PoteCoinService()
    coin = service.generate()
    print(coin)

def test_xmr_gen():
    service = XmrCoinService()
    coin = service.generate()
    print(coin)


def test_xrp_gen():
    service = RippleCoinService()
    coin = service.generate()
    print(coin)



def main():
    print("Hello world")

    test_bnb_gen()
    test_bsv_gen()
    test_club_gen()
    test_dash_gen()
    test_eos_gen()
    test_pote_gen()
    test_xmr_gen()
    test_xrp_gen()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# Needed dependenices: XMR, WAVES, USDT, EOS, BSV, ADA