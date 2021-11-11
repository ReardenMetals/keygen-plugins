from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins
import binascii

import re


class BscCoinService(CoinService):

    @staticmethod
    def get_currency_name():
        return "BSC"

    def generate(self):
        # Generate random mnemonic
        mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)

        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

        # Generate BIP44 master keys
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BINANCE_SMART_CHAIN)

        address = bip_obj_mst.PublicKey().ToAddress()
        wif = bip_obj_mst.PrivateKey().Raw().ToHex()
        seed = mnemonic

        return CryptoCoin(address, wif, seed)

    def get_coin(self, private_key):
        private_key_bytes = binascii.unhexlify(private_key)
        key_pair = Bip44.FromAddressPrivKey(private_key_bytes, Bip44Coins.BINANCE_SMART_CHAIN)
        address = key_pair.PublicKey().ToAddress()
        return CryptoCoin(address, private_key)

    def generate_asset_id(self, coin):
        return re.search('^0x(\\w{6}).+$', coin.address).group(1)


__all__ = ['BscCoinService']
