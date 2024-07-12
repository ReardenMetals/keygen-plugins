from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService

from bip_utils_2_9_3 import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip39WordsNum, Bip44, Bip44Coins
import codecs


class SolCoinService(CoinService):

    @staticmethod
    def get_currency_name():
        return "SOL"

    def generate(self):
        # Generate random mnemonic
        mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)
        print(f"Mnemonic string: {mnemonic}")
        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

        # The first 32-byte of the seed is the private key
        bip44_ctx = Bip44.FromPrivateKey(seed_bytes[:32], Bip44Coins.SOLANA)

        address = bip44_ctx.PublicKey().ToAddress()
        wif = bip44_ctx.PrivateKey().Raw().ToHex()
        seed = mnemonic

        return CryptoCoin(address, wif, seed)

    def get_coin(self, private_key):
        decoded_private_key = codecs.decode(private_key, 'hex')
        address = Bip44.FromPrivateKey(decoded_private_key, Bip44Coins.SOLANA).PublicKey().ToAddress()
        return CryptoCoin(address, private_key)


__all__ = ['SolCoinService']
