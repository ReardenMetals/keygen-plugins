from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService
from aioeos.keys import EosKey

import re


class EosCoinService(CoinService):

    @staticmethod
    def get_currency_name():
        return "EOS"

    def generate(self):
        eos = EosKey()
        address = eos.to_public()
        wif = eos.to_wif()
        seed = ''
        return CryptoCoin(address, wif, seed)

    def get_coin(self, private_key):
        eos = EosKey(private_key=private_key)
        address = eos.to_public()
        wif = eos.to_wif()
        seed = ''
        return CryptoCoin(address, wif, seed)

    def generate_asset_id(self, coin):
        return re.search('^EOS(\\w{6}).+$', coin.address).group(1)


__all__ = ['EosCoinService']
