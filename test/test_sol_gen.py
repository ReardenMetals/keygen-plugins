"""
Example of wallet creation in the same way of Solana-CLI.

Solana-CLI works differently from other wallets.
First of all, it's not a HD-wallet but it only generates a master key without deriving any child key.
Secondly, the master private key is just the first 32-byte of the seed generated from the mnemonic, it's not computing
the HMAC-SHA512 like BIP32.
"""

from bip_utils_2_9_3 import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip39WordsNum, Bip44, Bip44Coins
import codecs


# Generate random mnemonic
mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)
print(f"Mnemonic string: {mnemonic}")
# Generate seed from mnemonic
seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

# The first 32-byte of the seed is the private key
bip44_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA)
# Same address of Solana-CLI
print(f"Address: {bip44_ctx.PublicKey().ToAddress()}")
# Print master key, no need to derive any child key
print(f"Public key: {bip44_ctx.PublicKey().RawCompressed().ToHex()}")

wif = bip44_ctx.PrivateKey().Raw().ToHex()
print(f"Private key: {wif}")

decoded_private_key = codecs.decode(wif, 'hex')
print(f"Address From Priv: {Bip44.FromPrivateKey(decoded_private_key, Bip44Coins.SOLANA).PublicKey().ToAddress()}")