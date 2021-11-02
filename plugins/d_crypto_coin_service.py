from abc import ABC, abstractmethod
from enum import auto, Enum, unique, IntEnum

from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44Coins, WifDecoder, CoinNames, Bip32Conf, \
    NetVersions, KeyNetVersions, Bip44CoinNotAllowedError, Bip32, Bip44DepthError, Bip32Utils, BipCoinBase, \
    P2PKH
from bip_utils.bip.bip_keys import BipPublicKey, BipPrivateKey

from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService


@unique
class Bip44Coins(Enum):
    # Main nets
    DENARIUS = auto(),


class DenariusConf:
    """ Class container for Denarius configuration. """

    # Names
    NAMES = CoinNames("Denarius", "D")

    # BIP44 net versions (dgub / dgpv) - (tgub / tgpv)
    BIP44_KEY_NET_VER = Bip32Conf.KEY_NET_VER

    # BIP49 net versions (dgub / dgpv) - (tgub / tgpv)
    BIP49_KEY_NET_VER = NetVersions(KeyNetVersions(b"02facafd", b"02fac398"))

    # Versions for P2PKH address
    P2PKH_NET_VER = NetVersions(b"\x1e")
    # Versions for P2SH address
    P2SH_NET_VER = NetVersions(b"\x5A")
    # WIF net version
    WIF_NET_VER = NetVersions(b"\x9E")


class Bip44BaseConst:
    """ Class container for BIP44 base constants. """

    # Map from coin to index
    COIN_TO_IDX = \
        {
            # Main nets
            Bip44Coins.DENARIUS: 116,
        }


class Bip44Coin(BipCoinBase):
    """ Generic class for BIP-044 coins. """

    def __init__(self, coin_conf, is_testnet, addr_fct):
        super().__init__(coin_conf, coin_conf.BIP44_KEY_NET_VER, is_testnet, addr_fct)


# Configuration for Denarius main net
Bip44DenariusMainNet = Bip44Coin(coin_conf=DenariusConf,
                                 is_testnet=False,
                                 addr_fct=P2PKH)


class Bip44Const:
    """ Class container for BIP44 constants. """

    # Specification name
    SPEC_NAME = "BIP-0044"
    # Purpose
    PURPOSE = Bip32Utils.HardenIndex(44)
    # Allowed coins
    ALLOWED_COINS = \
        [
            Bip44Coins.DENARIUS,
        ]
    # Map from Bip44Coins to coin classes
    COIN_TO_CLASS = \
        {
            Bip44Coins.DENARIUS: Bip44DenariusMainNet,
        }


@unique
class Bip44Changes(IntEnum):
    """ Enumerative for BIP44 changes. """

    CHAIN_EXT = 0,
    CHAIN_INT = 1,


@unique
class Bip44Levels(IntEnum):
    """ Enumerative for BIP44 levels. """

    MASTER = 0,
    PURPOSE = 1,
    COIN = 2,
    ACCOUNT = 3,
    CHANGE = 4,
    ADDRESS_INDEX = 5,


class Bip44Base(ABC):

    @classmethod
    def FromSeed(cls, seed_bytes, coin_type):
        if not cls.IsCoinAllowed(coin_type):
            raise Bip44CoinNotAllowedError("Coin %s cannot derive from %s specification" % (coin_type, cls.SpecName()))
        return cls(Bip32.FromSeed(seed_bytes, cls._GetCoinClass(coin_type).KeyNetVersions()), coin_type)

    @classmethod
    def FromExtendedKey(cls, key_str, coin_type):
        if not cls.IsCoinAllowed(coin_type):
            raise Bip44CoinNotAllowedError("Coin %s cannot derive from %s specification" % (coin_type, cls.SpecName()))
        return cls(Bip32.FromExtendedKey(key_str, cls._GetCoinClass(coin_type).KeyNetVersions()), coin_type)

    @classmethod
    def FromAddressPrivKey(cls, key_bytes, coin_type):
        if not cls.IsCoinAllowed(coin_type):
            raise Bip44CoinNotAllowedError("Coin %s cannot derive from %s specification" % (coin_type, cls.SpecName()))
        return cls(
            Bip32(key_bytes, b"", Bip44Levels.ADDRESS_INDEX, key_net_ver=cls._GetCoinClass(coin_type).KeyNetVersions()),
            coin_type)

    def __init__(self, bip32_obj, coin_type):

        # If the Bip32 is public-only, the depth shall start from the account level because hardened derivation is
        # used below it, which is not possible with public keys
        if bip32_obj.IsPublicOnly():
            if bip32_obj.Depth() < Bip44Levels.ACCOUNT or \
                    bip32_obj.Depth() > Bip44Levels.ADDRESS_INDEX:
                raise Bip44DepthError(
                    "Depth of the public-only Bip32 object (%d) is below account level or beyond address index level" % bip32_obj.Depth())
        # If the Bip32 object is not public-only, any depth is fine as long as it is not greater than address index level
        else:
            if bip32_obj.Depth() > Bip44Levels.ADDRESS_INDEX:
                raise Bip44DepthError(
                    "Depth of the Bip32 object (%d) is beyond address index level" % bip32_obj.Depth())

        # Finally, initialize class
        self.m_bip32 = bip32_obj
        self.m_coin_type = coin_type
        self.m_coin_class = self._GetCoinClass(coin_type)

    def PublicKey(self):
        return BipPublicKey(self.m_bip32, self.m_coin_class)

    def PrivateKey(self):
        return BipPrivateKey(self.m_bip32, self.m_coin_class)

    def CoinClass(self):
        return self.m_coin_class

    def IsPublicOnly(self):
        return self.m_bip32.IsPublicOnly()

    def IsLevel(self, level_idx):
        if not isinstance(level_idx, Bip44Levels):
            raise TypeError("Level is not an enumerative of Bip44Levels")

        return self.m_bip32.Depth() == level_idx

    @classmethod
    def _PurposeGeneric(cls, bip_obj):
        if not cls.IsLevel(bip_obj, Bip44Levels.MASTER):
            raise Bip44DepthError("Current depth (%d) is not suitable for deriving purpose" % bip_obj.m_bip32.Depth())

        return cls(bip_obj.m_bip32.ChildKey(cls._GetPurpose()), bip_obj.m_coin_type)

    @classmethod
    def _CoinGeneric(cls, bip_obj):
        if not cls.IsLevel(bip_obj, Bip44Levels.PURPOSE):
            raise Bip44DepthError("Current depth (%d) is not suitable for deriving coin" % bip_obj.m_bip32.Depth())

        coin_idx = Bip44BaseConst.COIN_TO_IDX[bip_obj.m_coin_type]

        return cls(bip_obj.m_bip32.ChildKey(Bip32Utils.HardenIndex(coin_idx)), bip_obj.m_coin_type)

    @classmethod
    def _AccountGeneric(cls, bip_obj, acc_idx):
        if not cls.IsLevel(bip_obj, Bip44Levels.COIN):
            raise Bip44DepthError("Current depth (%d) is not suitable for deriving account" % bip_obj.m_bip32.Depth())

        return cls(bip_obj.m_bip32.ChildKey(Bip32Utils.HardenIndex(acc_idx)), bip_obj.m_coin_type)

    @classmethod
    def _ChangeGeneric(cls, bip_obj, change_idx):
        if not isinstance(change_idx, Bip44Changes):
            raise TypeError("Change index is not an enumerative of Bip44Changes")

        if not cls.IsLevel(bip_obj, Bip44Levels.ACCOUNT):
            raise Bip44DepthError("Current depth (%d) is not suitable for deriving change" % bip_obj.m_bip32.Depth())

        return cls(bip_obj.m_bip32.ChildKey(change_idx), bip_obj.m_coin_type)

    @classmethod
    def _AddressIndexGeneric(cls, bip_obj, addr_idx):
        if not cls.IsLevel(bip_obj, Bip44Levels.CHANGE):
            raise Bip44DepthError("Current depth (%d) is not suitable for deriving address" % bip_obj.m_bip32.Depth())

        return cls(bip_obj.m_bip32.ChildKey(addr_idx), bip_obj.m_coin_type)

    @abstractmethod
    def Purpose(self):
        pass

    @abstractmethod
    def Coin(self):
        pass

    @abstractmethod
    def Account(self, acc_idx):
        pass

    @abstractmethod
    def Change(self, change_idx):
        pass

    @abstractmethod
    def AddressIndex(self, addr_idx):
        pass

    @staticmethod
    @abstractmethod
    def SpecName():
        pass

    @staticmethod
    @abstractmethod
    def IsCoinAllowed(coin_type):
        pass

    @staticmethod
    @abstractmethod
    def _GetPurpose():
        pass

    @staticmethod
    @abstractmethod
    def _GetCoinClass(coin_type):
        pass


class Bip44(Bip44Base):

    def Purpose(self):
        return self._PurposeGeneric(self)

    def Coin(self):
        return self._CoinGeneric(self)

    def Account(self, acc_idx):
        return self._AccountGeneric(self, acc_idx)

    def Change(self, change_idx):
        return self._ChangeGeneric(self, change_idx)

    def AddressIndex(self, addr_idx):
        return self._AddressIndexGeneric(self, addr_idx)

    @staticmethod
    def SpecName():
        return Bip44Const.SPEC_NAME

    @staticmethod
    def IsCoinAllowed(coin_type):
        if not isinstance(coin_type, Bip44Coins):
            raise TypeError("Coin is not an enumerative of Bip44Coins")

        return coin_type in Bip44Const.ALLOWED_COINS

    @staticmethod
    def _GetPurpose():
        return Bip44Const.PURPOSE

    @staticmethod
    def _GetCoinClass(coin_type):
        return Bip44Const.COIN_TO_CLASS[coin_type]


class DenariusCoinService(CoinService):

    @staticmethod
    def get_currency_name():
        return "DENARIUS"

    def generate(self, ):
        # Generate random mnemonic
        mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)

        return self.generate_from_mnemonic(mnemonic)

    def generate_from_mnemonic(self, mnemonic: str):
        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

        # Generate BIP44 master keys
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.DENARIUS)

        address = bip_obj_mst.PublicKey().ToAddress()
        wif = bip_obj_mst.PrivateKey().ToWif()
        seed = mnemonic

        return CryptoCoin(address, wif, seed)

    def get_coin(self, private_key):
        decoded_wif = WifDecoder.Decode(wif_str=private_key, net_addr_ver=DenariusConf.WIF_NET_VER.Main())
        key_pair = Bip44.FromAddressPrivKey(decoded_wif, Bip44Coins.DENARIUS)
        address = key_pair.PublicKey().ToAddress()
        return CryptoCoin(address, private_key)


__all__ = ['DenariusCoinService']
