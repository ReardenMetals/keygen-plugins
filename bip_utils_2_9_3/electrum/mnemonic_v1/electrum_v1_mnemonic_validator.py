# Copyright (c) 2022 Emanuele Bellocchia
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

"""Module for Electrum v1 mnemonic validation."""

# Imports
from typing import Optional

from bip_utils_2_9_3.electrum.mnemonic_v1.electrum_v1_mnemonic import ElectrumV1Languages
from bip_utils_2_9_3.electrum.mnemonic_v1.electrum_v1_mnemonic_decoder import ElectrumV1MnemonicDecoder
from bip_utils_2_9_3.utils.mnemonic import MnemonicValidator


class ElectrumV1MnemonicValidator(MnemonicValidator):
    """
    Electrum v1 mnemonic validator class.
    It validates a mnemonic phrase.
    """

    m_mnemonic_decoder: ElectrumV1MnemonicDecoder

    def __init__(self,
                 lang: Optional[ElectrumV1Languages] = ElectrumV1Languages.ENGLISH) -> None:
        """
        Construct class.
        Language is set to English by default because Electrum v1 mnemonic only support one language,
        so it's useless (and slower) to automatically detect the language.

        Args:
            lang (ElectrumV1Languages, optional): Language, None for automatic detection
        """
        super().__init__(ElectrumV1MnemonicDecoder(lang))
