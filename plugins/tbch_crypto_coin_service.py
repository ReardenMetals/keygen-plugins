from keygen.crypto_coin_service import CoinService
from bip_utils.utils import CryptoUtils
from cashaddress import convert
from keygen.crypto_coin import CryptoCoin
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, BitcoinConf, Bip44Coins, WifDecoder, Bip44, \
    Base58Encoder, BitcoinCashConf

from keygen.wif_validator import is_compressed_wif


class BchCoinService(CoinService):

    @staticmethod
    def get_currency_name():
        return "tBCH"

    def generate(self):
        # Generate random mnemonic
        mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)

        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

        # Generate BIP44 master keys
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN_CASH_TESTNET)

        address = bip_obj_mst.PublicKey().ToAddress().replace('bchtest:', '')
        wif = bip_obj_mst.PrivateKey().ToWif()
        seed = mnemonic

        return CryptoCoin(address, wif, seed)

    def get_coin(self, private_key):
        return self.get_default_coin(private_key)

    @staticmethod
    def get_default_coin(private_key):
        decoded_wif = WifDecoder.Decode(wif_str=private_key, net_addr_ver=BitcoinCashConf.WIF_NET_VER.Test())
        key_pair = Bip44.FromAddressPrivKey(decoded_wif, Bip44Coins.BITCOIN_CASH_TESTNET)
        address = key_pair.PublicKey().ToAddress().replace('bitcoincash:', '')
        return CryptoCoin(address, private_key)


