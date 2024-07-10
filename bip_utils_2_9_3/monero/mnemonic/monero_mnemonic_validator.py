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

"""Module for Monero mnemonic validation."""

# Imports
from typing import Optional

from bip_utils_2_9_3.monero.mnemonic.monero_mnemonic import MoneroLanguages
from bip_utils_2_9_3.monero.mnemonic.monero_mnemonic_decoder import MoneroMnemonicDecoder
from bip_utils_2_9_3.utils.mnemonic import MnemonicValidator


class MoneroMnemonicValidator(MnemonicValidator):
    """
    Monero mnemonic validator class.
    It validates a mnemonic phrase.
    """

    def __init__(self,
                 lang: Optional[MoneroLanguages] = None) -> None:
        """
        Construct class.

        Args:
            lang (MoneroLanguages, optional): Language, None for automatic detection
        """
        super().__init__(MoneroMnemonicDecoder(lang))
