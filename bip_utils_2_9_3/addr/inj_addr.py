# Copyright (c) 2021 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
Module for Injective address encoding/decoding.
Reference: https://docs.injective.network/learn/basic-concepts/accounts
"""

# Imports
from typing import Any, Union

from bip_utils_2_9_3.addr.addr_dec_utils import AddrDecUtils
from bip_utils_2_9_3.addr.addr_key_validator import AddrKeyValidator
from bip_utils_2_9_3.addr.eth_addr import EthAddrConst, EthAddrEncoder
from bip_utils_2_9_3.addr.iaddr_decoder import IAddrDecoder
from bip_utils_2_9_3.addr.iaddr_encoder import IAddrEncoder
from bip_utils_2_9_3.bech32 import Bech32ChecksumError, Bech32Decoder, Bech32Encoder
from bip_utils_2_9_3.coin_conf.coins_conf import CoinsConf
from bip_utils_2_9_3.ecc import IPublicKey
from bip_utils_2_9_3.utils.misc import BytesUtils


class InjAddrDecoder(IAddrDecoder):
    """
    Injective address decoder class.
    It allows the Injective address decoding.
    """

    @staticmethod
    def DecodeAddr(addr: str,
                   **kwargs: Any) -> bytes:
        """
        Decode an Algorand address to bytes.

        Args:
            addr (str): Address string

        Returns:
            bytes: Public key hash bytes

        Raises:
            ValueError: If the address encoding is not valid
        """
        try:
            addr_dec_bytes = Bech32Decoder.Decode(
                CoinsConf.Injective.ParamByKey("addr_hrp"),
                addr
            )
        except Bech32ChecksumError as ex:
            raise ValueError("Invalid bech32 checksum") from ex

        AddrDecUtils.ValidateLength(addr_dec_bytes,
                                    EthAddrConst.ADDR_LEN // 2)
        return addr_dec_bytes


class InjAddrEncoder(IAddrEncoder):
    """
    Injective address encoder class.
    It allows the Injective address encoding.
    """

    @staticmethod
    def EncodeKey(pub_key: Union[bytes, IPublicKey],
                  **kwargs: Any) -> str:
        """
        Encode a public key to Injective address.

        Args:
            pub_key (bytes or IPublicKey): Public key bytes or object

        Returns:
            str: Address string

        Raises:
            ValueError: If the public key is not valid
            TypeError: If the public key is not secp256k1
        """
        pub_key_obj = AddrKeyValidator.ValidateAndGetSecp256k1Key(pub_key)
        eth_addr = EthAddrEncoder.EncodeKey(pub_key_obj)
        return Bech32Encoder.Encode(CoinsConf.Injective.ParamByKey("addr_hrp"),
                                    BytesUtils.FromHexString(eth_addr[2:]))


# Deprecated: only for compatibility, Encoder class shall be used instead
InjAddr = InjAddrEncoder