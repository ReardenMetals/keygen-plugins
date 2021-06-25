from keygen.crypto_coin_factory import CoinFactory
from plugins.bnb_crypto_coin_service import BnbCoinService
from plugins.dash_crypto_coin_service import DashCoinService
from plugins.pote_crypto_coin_service import PoteCoinService
from plugins.xrp_crypto_coin_service import RippleCoinService


class CoinFactoryExtended(CoinFactory):
    def __init__(self):
        super().__init__()

    def get_available_currencies(self):
        return super().get_default_available_currencies() + CoinFactoryExtended.get_default_available_currencies()

    @staticmethod
    def get_default_available_currencies():
        return ['DASH', 'XRP', 'BNB', 'POTE']
        # return ['DASH', 'BSV', 'XRP', 'XMR', 'BNB', 'EOS', 'POTE', 'ADA'] # For the next release.

    def get_coin_service(self, currency):
        if currency == "DASH":
            return DashCoinService()
        if currency == "XRP":
            return RippleCoinService()
        if currency == "BNB":
            return BnbCoinService()
        if currency == "POTE":
            return PoteCoinService()
        return super().get_coin_service(currency)
