from keygen.crypto_coin_factory import CoinFactory
from plugins.ada_crypto_coin_service import CardanoCoinService
from plugins.bnb_crypto_coin_service import BnbCoinService
from plugins.bsv_crypto_coin_service import BsvCoinService
from plugins.dash_crypto_coin_service import DashCoinService
from plugins.eos_crypto_coin_service import EosCoinService
from plugins.pote_crypto_coin_service import PoteCoinService
from plugins.xmr_crypto_coin_service import XmrCoinService
from plugins.xrp_crypto_coin_service import RippleCoinService


class CoinFactoryExtended(CoinFactory):
    def __init__(self):
        super().__init__()

    def get_available_currencies(self):
        return super().get_default_available_currencies() + CoinFactoryExtended.get_default_available_currencies()

    @staticmethod
    def get_default_available_currencies():
        return ['DASH', 'BSV', 'XRP', 'XMR', 'BNB', 'EOS', 'POTE', 'ADA'] # For the next release.

    def get_coin_service(self, currency):
        if currency == "DASH":
            return DashCoinService()
        if currency == "BSV":
            return BsvCoinService()
        if currency == "XRP":
            return RippleCoinService()
        if currency == "XMR":
            return XmrCoinService()
        if currency == "BNB":
            return BnbCoinService()
        if currency == "EOS":
            return EosCoinService()
        if currency == "POTE":
            return PoteCoinService()
        if currency == "ADA":
            return CardanoCoinService()
        return super().get_coin_service(currency)
