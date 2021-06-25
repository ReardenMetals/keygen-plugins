# Keygen plugins module for generating crypto wallets
Python desktop offline application for generating Cold Storage Coins of different currencies: DASH, BSV, XRP, XMR, BNB, EOS, POTE, ADA

## Install keygen-plugins module:

Required Python version 3.8 (preferred Python 3.8.6)

Python-3.8.6 download link: https://www.python.org/downloads/release/python-386/

Install Keygen-Core: https://github.com/ReardenMetals/keygen-core

Download archive with the latest release of "Source Code (zip)" for Windows based system or "Source Code (tar.gz)" for Unix based system https://github.com/ReardenMetals/keygen-plugins/releases

Run the python scipt to test the the keypair generation:

    python main.py
    
## Third party libraries integrated into Keygen-plugins.

### aioeos library

https://pypi.org/project/aioeos/

Async Python library for interacting with EOS.io blockchain.

### base58 library

https://pypi.org/project/base58/

Base58 and Base58Check implementation compatible with what is used by the bitcoin network. Any other alternative alphabet (like the XRP one) can be used.

### cbor library

https://pypi.org/project/cbor/

An implementation of RFC 7049 - Concise Binary Object Representation (CBOR).

CBOR is comparable to JSON, has a superset of JSON’s ability, but serializes to a binary format which is smaller and faster to generate and parse.

The two primary functions are cbor.loads() and cbor.dumps().

This library includes a C implementation which runs 3-5 times faster than the Python standard library’s C-accelerated implementanion of JSON. This is also includes a 100% Python implementation.

### ed25519 library

https://pypi.org/project/ed25519/

Python bindings to the Ed25519 public-key signature system.

This offers a comfortable python interface to a C implementation of the Ed25519 public-key signature system (http://ed25519.cr.yp.to/), using the portable ‘ref’ code from the ‘SUPERCOP’ benchmarking suite.

This system provides high (128-bit) security, short (32-byte) keys, short (64-byte) signatures, and fast (2-6ms) operation. Please see the README for more details.

### monero library

https://pypi.org/project/monero/

A comprehensive Python module for handling Monero cryptocurrency.

### scrypt library

https://pypi.org/project/scrypt/

This is a set of Python bindings for the scrypt key derivation function.

Scrypt is useful when encrypting password as it is possible to specify a minimum amount of time to use when encrypting and decrypting. If, for example, a password takes 0.05 seconds to verify, a user won’t notice the slight delay when signing in, but doing a brute force search of several billion passwords will take a considerable amount of time. This is in contrast to more traditional hash functions such as MD5 or the SHA family which can be implemented extremely fast on cheap hardware.








