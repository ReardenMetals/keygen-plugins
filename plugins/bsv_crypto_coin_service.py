from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService

from bip_utils import Bip44Coins, WifDecoder, Bip44, Bip39MnemonicGenerator, \
    Bip39SeedGenerator, BitcoinSvConf


class BsvCoinService(CoinService):

    @staticmethod
    def get_currency_name():
        return "BSV"

    def generate(self):
        # Generate random mnemonic
        mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)

        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

        # Generate BIP44 master keys
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN_SV)

        address = bip_obj_mst.PublicKey().ToAddress()
        wif = bip_obj_mst.PrivateKey().ToWif()
        seed = mnemonic

        return CryptoCoin(address, wif, seed)

    def get_coin(self, private_key):
        decoded_wif = WifDecoder.Decode(wif_str=private_key, net_addr_ver=BitcoinSvConf.WIF_NET_VER.Main())
        key_pair = Bip44.FromAddressPrivKey(decoded_wif, Bip44Coins.BITCOIN_SV)
        address = key_pair.PublicKey().ToAddress()
        return CryptoCoin(address, private_key)


__all__ = ['BsvCoinService']
