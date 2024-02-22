from abc import ABC, abstractmethod
from enum import auto, Enum, unique, IntEnum

from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44Coins, WifDecoder, CoinNames, Bip32Conf, \
    NetVersions, KeyNetVersions, Bip44CoinNotAllowedError, Bip32, Bip44DepthError, Bip32Utils, Bip44Coin, BipCoinBase, \
    P2PKH
from bip_utils.bip.bip_keys import BipPublicKey, BipPrivateKey

from keygen.crypto_coin import CryptoCoin
from keygen.crypto_coin_service import CoinService


@unique
class Bip44Coins(Enum):
    """ Enumerative for supported BIP44 coins.
    The indexes are just dummy values, they are converted to BIP44 indexes using the COIN_TO_IDX dictionary.
    """

    # Main nets
    BITCOIN              = auto(),
    BITCOIN_CASH         = auto(),
    BITCOIN_SV           = auto(),
    LITECOIN             = auto(),
    TEXITCOIN             = auto(),
    DOGECOIN             = auto(),
    DASH                 = auto(),
    ZCASH                = auto(),
    ETHEREUM             = auto(),
    ETHEREUM_CLASSIC     = auto(),
    RIPPLE               = auto(),
    TRON                 = auto(),
    VECHAIN              = auto(),
    COSMOS               = auto(),
    BAND_PROTOCOL        = auto(),
    KAVA                 = auto(),
    IRIS_NET             = auto(),
    BINANCE_CHAIN        = auto(),
    BINANCE_SMART_CHAIN  = auto(),
    NINE_CHRONICLES_GOLD = auto(),
    # Test nets
    BITCOIN_TESTNET      = auto(),
    LITECOIN_TESTNET     = auto(),
    DOGECOIN_TESTNET     = auto(),
    DASH_TESTNET         = auto(),
    BITCOIN_CASH_TESTNET = auto(),
    BITCOIN_SV_TESTNET   = auto(),
    ZCASH_TESTNET        = auto(),

class Bip44Coin(BipCoinBase):
    """ Generic class for BIP-044 coins. """

    def __init__(self, coin_conf, is_testnet, addr_fct):
        """ Construct class.

        Args:
            coin_conf (class): Coin configuration class
            is_testnet (bool): True if test net, false otherwise
            addr_fct (class) : Address class
        """
        super().__init__(coin_conf, coin_conf.BIP44_KEY_NET_VER, is_testnet, addr_fct)


class BitcoinConf:
    """ Class container for Bitcoin configuration. """

    # Names
    NAMES             = CoinNames("Bitcoin"        , "BTC")
    # Test names
    TEST_NAMES        = CoinNames("Bitcoin TestNet", "BTC")

    # BIP44 net versions (same of BIP32)
    BIP44_KEY_NET_VER = Bip32Conf.KEY_NET_VER
    # BIP49 net versions (ypub / yprv) - (upub / uprv)
    BIP49_KEY_NET_VER = NetVersions(KeyNetVersions(b"049d7cb2", b"049d7878"),
                                    KeyNetVersions(b"044a5262", b"044a4e28"))
    # BIP84 net versions (zpub / zprv) -  (vpub / vprv)
    BIP84_KEY_NET_VER = NetVersions(KeyNetVersions(b"04b24746", b"04b2430c"),
                                    KeyNetVersions(b"045f1cf6", b"045f18bc"))

    # Versions for P2PKH address
    P2PKH_NET_VER     = NetVersions(b"\x00", b"\x6f")
    # Versions for P2SH address
    P2SH_NET_VER      = NetVersions(b"\x05", b"\xc4")
    # Versions for P2WPKH address
    P2WPKH_NET_VER    = NetVersions("bc", "tb")
    # WIF net version
    WIF_NET_VER       = NetVersions(b"\x80", b"\xef")

class TexitCoinConf:
    """ Class container for TexitCoin configuration. """

    # Names
    NAMES = CoinNames("TexitCoin", "TXC")

    # False for using Bitcoin net versions for extended keys (xprv/xpub and similar), true for using the alternate ones (Ltpv/Ltub and similar)
    EX_KEY_ALT = False
    # False for using P2SH deprecated addresses, true for the new addresses
    P2SH_DEPR_ADDR = False

    # BIP44 net versions
    # Litecoin can have 2 different main version: same of Bitcoin or (Ltpv / Ltub), whereas test net version is always (ttub / ttpv)
    BIP44_KEY_NET_VER = NetVersions(
        {"btc": BitcoinConf.BIP44_KEY_NET_VER.Main(), "alt": KeyNetVersions(b"019da462", b"019d9cfe")},
        KeyNetVersions(b"0436f6e1", b"0436ef7d"))
    # BIP49 net versions
    # Litecoin can have 2 different main version: same of Bitcoin or (Mtpv / Mtub), whereas test net version is always (ttub / ttpv)
    BIP49_KEY_NET_VER = NetVersions(
        {"btc": BitcoinConf.BIP49_KEY_NET_VER.Main(), "alt": KeyNetVersions(b"01b26ef6", b"01b26792")},
        KeyNetVersions(b"0436f6e1", b"0436ef7d"))
    # BIP84 net versions (zpub / zprv) - (ttub / ttpv)
    BIP84_KEY_NET_VER = NetVersions(BitcoinConf.BIP84_KEY_NET_VER.Main(),
                                    KeyNetVersions(b"0436f6e1", b"0436ef7d"))

    # Versions for P2PKH address
    P2PKH_NET_VER = NetVersions(b"\x30", b"\x6f")
    # Deprecated versions for P2SH address (same of Bitcoin)
    P2SH_DEPR_NET_VER = BitcoinConf.P2SH_NET_VER
    # Versions for P2SH address
    P2SH_NET_VER = NetVersions(b"\x32", b"\x3a")
    # Versions for P2WPKH address
    P2WPKH_NET_VER = NetVersions("txc", "ttxc")

    # WIF net version
    WIF_NET_VER = NetVersions(b"\xc1", b"\xef")

# Configuration for TexitCoin main net
Bip44TexitCoinMainNet = Bip44Coin(coin_conf  = TexitCoinConf,
                                 is_testnet = False,
                                 addr_fct   = P2PKH)

class Bip44Const:
    """ Class container for BIP44 constants. """

    # Specification name
    SPEC_NAME = "BIP-0044"
    # Purpose
    PURPOSE   = Bip32Utils.HardenIndex(44)
    # Allowed coins
    ALLOWED_COINS = \
        [
            Bip44Coins.BITCOIN            , Bip44Coins.BITCOIN_TESTNET,
            Bip44Coins.BITCOIN_CASH       , Bip44Coins.BITCOIN_CASH_TESTNET,
            Bip44Coins.BITCOIN_SV         , Bip44Coins.BITCOIN_SV_TESTNET,
            Bip44Coins.LITECOIN           , Bip44Coins.LITECOIN_TESTNET,
            Bip44Coins.DOGECOIN           , Bip44Coins.DOGECOIN_TESTNET,
            Bip44Coins.DASH               , Bip44Coins.DASH_TESTNET,
            Bip44Coins.ZCASH              , Bip44Coins.ZCASH_TESTNET,
            Bip44Coins.ETHEREUM           ,
            Bip44Coins.ETHEREUM_CLASSIC   ,
            Bip44Coins.RIPPLE             ,
            Bip44Coins.TRON               ,
            Bip44Coins.VECHAIN            ,
            Bip44Coins.COSMOS             ,
            Bip44Coins.BAND_PROTOCOL      ,
            Bip44Coins.KAVA               ,
            Bip44Coins.IRIS_NET           ,
            Bip44Coins.BINANCE_CHAIN      ,
            Bip44Coins.BINANCE_SMART_CHAIN,
            Bip44Coins.NINE_CHRONICLES_GOLD,
            Bip44Coins.TEXITCOIN,
        ]
    # Map from Bip44Coins to coin classes
    COIN_TO_CLASS = \
        {
            Bip44Coins.TEXITCOIN              : Bip44TexitCoinMainNet,

        }








@unique
class Bip44Changes(IntEnum):
    """ Enumerative for BIP44 changes. """

    CHAIN_EXT = 0,
    CHAIN_INT = 1,


@unique
class Bip44Levels(IntEnum):
    """ Enumerative for BIP44 levels. """

    MASTER        = 0,
    PURPOSE       = 1,
    COIN          = 2,
    ACCOUNT       = 3,
    CHANGE        = 4,
    ADDRESS_INDEX = 5,


class Bip44BaseConst:
    """ Class container for BIP44 base constants. """

    # Map from coin to index
    COIN_TO_IDX = \
    {
        # Main nets
        Bip44Coins.BITCOIN              : 0,
        Bip44Coins.LITECOIN             : 2,
        Bip44Coins.TEXITCOIN             : 116, #TODO FIX THIS
        Bip44Coins.DOGECOIN             : 3,
        Bip44Coins.DASH                 : 5,
        Bip44Coins.ETHEREUM             : 60,
        Bip44Coins.BINANCE_SMART_CHAIN  : 60,
        Bip44Coins.ETHEREUM_CLASSIC     : 61,
        Bip44Coins.COSMOS               : 118,
        Bip44Coins.IRIS_NET             : 118,
        Bip44Coins.ZCASH                : 133,
        Bip44Coins.RIPPLE               : 144,
        Bip44Coins.BITCOIN_CASH         : 145,
        Bip44Coins.TRON                 : 195,
        Bip44Coins.BITCOIN_SV           : 236,
        Bip44Coins.BAND_PROTOCOL        : 494,
        Bip44Coins.KAVA                 : 494,
        Bip44Coins.NINE_CHRONICLES_GOLD : 567,
        Bip44Coins.BINANCE_CHAIN        : 714,
        Bip44Coins.VECHAIN              : 818,
        # Test nets
        Bip44Coins.BITCOIN_TESTNET      : 1,
        Bip44Coins.LITECOIN_TESTNET     : 1,
        Bip44Coins.DOGECOIN_TESTNET     : 1,
        Bip44Coins.DASH_TESTNET         : 1,
        Bip44Coins.BITCOIN_CASH_TESTNET : 1,
        Bip44Coins.BITCOIN_SV_TESTNET   : 1,
        Bip44Coins.ZCASH_TESTNET        : 1,
    }


class Bip44Base(ABC):
    """ BIP44 base class.
    It allows coin, account, chain and address keys generation in according to BIP44 or its extension (e.g. BIP49, BIP84).
    The class is meant to be derived by classes implementing BIP44 or its extension.
    """

    #
    # Class methods for construction
    #

    @classmethod
    def FromSeed(cls, seed_bytes, coin_type):
        """ Create a Bip object (e.g. BIP44, BIP49, BIP84) from the specified seed (e.g. BIP39 seed).
        The test net flag is automatically set when the coin is derived. However, if you want to get the correct master
        or purpose keys, you have to specify here if it's a test net.

        Args:
            seed_bytes (bytes)   : Seed bytes
            coin_type (Bip44Coins): Coin type, must be a Bip44Coins enum

        Returns:
            Bip object: Bip object

        Raises:
            TypeError: If coin index is not a Bip44Coins enum
            ValueError: If the seed is too short
            Bip44CoinNotAllowedError: If the coin is not allowed to derive from the BIP specification
            Bip32KeyError: If the seed is not suitable for master key generation
        """
        if not cls.IsCoinAllowed(coin_type):
            raise Bip44CoinNotAllowedError("Coin %s cannot derive from %s specification" % (coin_type, cls.SpecName()))
        return cls(Bip32.FromSeed(seed_bytes, cls._GetCoinClass(coin_type).KeyNetVersions()), coin_type)

    @classmethod
    def FromExtendedKey(cls, key_str, coin_type):
        """ Create a Bip object (e.g. BIP44, BIP49, BIP84) from the specified extended key.

        Args:
            key_str (str)        : Extended key string
            coin_type (Bip44Coins): Coin type, must be a Bip44Coins enum

        Returns:
            Bip object: Bip object

        Raises:
            TypeError: If coin index is not a Bip44Coins enum
            Bip44CoinNotAllowedError: If the coin is not allowed to derive from the BIP specification
            Bip32KeyError: If the extended key is not valid
        """
        if not cls.IsCoinAllowed(coin_type):
            raise Bip44CoinNotAllowedError("Coin %s cannot derive from %s specification" % (coin_type, cls.SpecName()))
        return cls(Bip32.FromExtendedKey(key_str, cls._GetCoinClass(coin_type).KeyNetVersions()), coin_type)

    @classmethod
    def FromAddressPrivKey(cls, key_bytes, coin_type):
        """ Create a Bip object (e.g. BIP44, BIP49, BIP84) from the specified private key related to an address.

        Args:
            key_bytes (bytes)     : Key bytes
            coin_type (Bip44Coins): Coin type, must be a Bip44Coins enum

        Returns:
            Bip object: Bip object

        Raises:
            TypeError: If coin index is not a Bip44Coins enum
            Bip44CoinNotAllowedError: If the coin is not allowed to derive from the BIP specification
            Bip32KeyError: If the key is not valid
        """
        if not cls.IsCoinAllowed(coin_type):
            raise Bip44CoinNotAllowedError("Coin %s cannot derive from %s specification" % (coin_type, cls.SpecName()))
        return cls(Bip32(key_bytes, b"", Bip44Levels.ADDRESS_INDEX, key_net_ver=cls._GetCoinClass(coin_type).KeyNetVersions()), coin_type)

    #
    # Public methods
    #

    def __init__(self, bip32_obj, coin_type):
        """ Construct class from a Bip32 object and coin type.

        Args:
            bip32_obj (Bip32 object): Bip32 object
            coin_type (Bip44Coins)  : Coin type, must be a Bip44Coins enum

        Returns:
            Bip44DepthError: If the Bip32 object depth is not valid
        """

        # If the Bip32 is public-only, the depth shall start from the account level because hardened derivation is
        # used below it, which is not possible with public keys
        if bip32_obj.IsPublicOnly():
            if bip32_obj.Depth() < Bip44Levels.ACCOUNT or \
               bip32_obj.Depth() > Bip44Levels.ADDRESS_INDEX:
                raise Bip44DepthError("Depth of the public-only Bip32 object (%d) is below account level or beyond address index level" % bip32_obj.Depth())
        # If the Bip32 object is not public-only, any depth is fine as long as it is not greater than address index level
        else:
            if bip32_obj.Depth() > Bip44Levels.ADDRESS_INDEX:
                raise Bip44DepthError("Depth of the Bip32 object (%d) is beyond address index level" % bip32_obj.Depth())

        # Finally, initialize class
        self.m_bip32      = bip32_obj
        self.m_coin_type  = coin_type
        self.m_coin_class = self._GetCoinClass(coin_type)

    def PublicKey(self):
        """ Return the public key.

        Returns:
            BipPublicKey object: BipPublicKey object

        """
        return BipPublicKey(self.m_bip32, self.m_coin_class)

    def PrivateKey(self):
        """ Return the private key.

        Returns:
            BipPrivateKey object: BipPrivateKey object

        Raises:
            Bip32KeyError: If the Bip32 object is public-only
        """
        return BipPrivateKey(self.m_bip32, self.m_coin_class)

    def CoinClass(self):
        """ Get coin class.

        Returns:
            BipCoinBase child object: BipCoinBase child object
        """
        return self.m_coin_class

    def IsPublicOnly(self):
        """ Get if it's public-only.

        Returns:
            bool: True if public-only, false otherwise
        """
        return self.m_bip32.IsPublicOnly()

    def IsLevel(self, level_idx):
        """ Return if the current depth is the specified one.

        Args:
            level_idx (int): Level to be checked

        Returns:
            bool: True if it's the specified level, false otherwise

        Raises:
            TypeError: If the level index is not a Bip44Levels enum
        """
        if not isinstance(level_idx, Bip44Levels):
            raise TypeError("Level is not an enumerative of Bip44Levels")

        return self.m_bip32.Depth() == level_idx

    #
    # Class methods ("protected", in the sense that they are called only internally)
    #

    @classmethod
    def _PurposeGeneric(cls, bip_obj):
        """ Derive a child key from the purpose and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It shall be called from a child class.

        Args:
            bip_obj (Bip44Base child object): Bip44Base child object (e.g. BIP44, BIP49, BIP84)

        Returns:
            Bip44Base child object: Bip44Base child object

        Raises:
            Bip44DepthError: If the current depth is not suitable for deriving keys
            Bip32KeyError: If the derivation results in an invalid key
        """
        if not cls.IsLevel(bip_obj, Bip44Levels.MASTER):
            raise Bip44DepthError("Current depth (%d) is not suitable for deriving purpose" % bip_obj.m_bip32.Depth())

        return cls(bip_obj.m_bip32.ChildKey(cls._GetPurpose()), bip_obj.m_coin_type)

    @classmethod
    def _CoinGeneric(cls, bip_obj):
        """ Derive a child key from the coin type specified at construction and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It shall be called from a child class.

        Args:
            bip_obj (Bip44Base child object): Bip44Base child object (e.g. BIP44, BIP49, BIP84)

        Returns:
            Bip44Base child object: Bip44Base child object

        Raises:
            Bip44DepthError: If the current depth is not suitable for deriving keys
            Bip32KeyError: If the derivation results in an invalid key
        """
        if not cls.IsLevel(bip_obj, Bip44Levels.PURPOSE):
            raise Bip44DepthError("Current depth (%d) is not suitable for deriving coin" % bip_obj.m_bip32.Depth())

        coin_idx = Bip44BaseConst.COIN_TO_IDX[bip_obj.m_coin_type]

        return cls(bip_obj.m_bip32.ChildKey(Bip32Utils.HardenIndex(coin_idx)), bip_obj.m_coin_type)

    @classmethod
    def _AccountGeneric(cls, bip_obj, acc_idx):
        """ Derive a child key from the specified account index and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It shall be called from a child class.

        Args:
            bip_obj (Bip44Base child object): Bip44Base child object (e.g. BIP44, BIP49, BIP84)
            acc_idx (int)                   : Account index

        Returns:
            Bip44Base child object: Bip44Base child object

        Raises:
            Bip44DepthError: If the current depth is not suitable for deriving keys
            Bip32KeyError: If the derivation results in an invalid key
        """
        if not cls.IsLevel(bip_obj, Bip44Levels.COIN):
            raise Bip44DepthError("Current depth (%d) is not suitable for deriving account" % bip_obj.m_bip32.Depth())

        return cls(bip_obj.m_bip32.ChildKey(Bip32Utils.HardenIndex(acc_idx)), bip_obj.m_coin_type)

    @classmethod
    def _ChangeGeneric(cls, bip_obj, change_idx):
        """ Derive a child key from the specified chain type and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It shall be called from a child class.

        Args:
            bip_obj (Bip44Base child object): Bip44Base child object (e.g. BIP44, BIP49, BIP84)
            change_idx (Bip44Changes)       : change index, must a Bip44Changes enum

        Returns:
            Bip44Base child object: Bip44Base child object

        Raises:
            TypeError: If chain index is not a Bip44Changes enum
            Bip44DepthError: If the current depth is not suitable for deriving keys
            Bip32KeyError: If the derivation results in an invalid key
        """
        if not isinstance(change_idx, Bip44Changes):
            raise TypeError("Change index is not an enumerative of Bip44Changes")

        if not cls.IsLevel(bip_obj, Bip44Levels.ACCOUNT):
            raise Bip44DepthError("Current depth (%d) is not suitable for deriving change" % bip_obj.m_bip32.Depth())

        return cls(bip_obj.m_bip32.ChildKey(change_idx), bip_obj.m_coin_type)

    @classmethod
    def _AddressIndexGeneric(cls, bip_obj, addr_idx):
        """ Derive a child key from the specified address index and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It shall be called from a child class.

        Args:
            bip_obj (Bip44Base child object): Bip44Base child object (e.g. BIP44, BIP49, BIP84)
            addr_idx (int)                  : Address index

        Returns:
            Bip44Base child object: Bip44Base child object

        Raises:
            Bip44DepthError: If the current depth is not suitable for deriving keys
            Bip32KeyError: If the derivation results in an invalid key
        """
        if not cls.IsLevel(bip_obj, Bip44Levels.CHANGE):
            raise Bip44DepthError("Current depth (%d) is not suitable for deriving address" % bip_obj.m_bip32.Depth())

        return cls(bip_obj.m_bip32.ChildKey(addr_idx), bip_obj.m_coin_type)

    #
    # Abstract methods
    #

    @abstractmethod
    def Purpose(self):
        """ Derive a child key from the purpose and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It calls the underlying _PurposeGeneric method with the current object as parameter.

        Returns:
            Bip44Base child object: Bip44Base child object

        Raises:
            Bip44DepthError: If current depth is not suitable for deriving keys
            Bip32KeyError: If the derivation results in an invalid key
        """
        pass

    @abstractmethod
    def Coin(self):
        """ Derive a child key from the coin type specified at construction and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It calls the underlying _CoinGeneric method with the current object as parameter.

        Returns:
            Bip44Base child object: Bip44Base child object

        Raises:
            Bip44DepthError: If current depth is not suitable for deriving keys
            Bip32KeyError: If the derivation results in an invalid key
        """
        pass

    @abstractmethod
    def Account(self, acc_idx):
        """ Derive a child key from the specified account index and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It calls the underlying _AccountGeneric method with the current object as parameter.

        Args:
            acc_idx (int): Account index

        Returns:
            Bip44Base child object: Bip44Base child object

        Raises:
            Bip44DepthError: If current depth is not suitable for deriving keys
            Bip32KeyError: If the derivation results in an invalid key
        """
        pass

    @abstractmethod
    def Change(self, change_idx):
        """ Derive a child key from the specified account index and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It calls the underlying _ChangeGeneric method with the current object as parameter.

        Args:
            change_idx (Bip44Changes): Change index, must a Bip44Changes enum

        Returns:
            Bip44Base child object: Bip44Base child object

        Raises:
            TypeError: If chain index is not a Bip44Changes enum
            Bip44DepthError: If current depth is not suitable for deriving keys
            Bip32KeyError: If the derivation results in an invalid key
        """
        pass

    @abstractmethod
    def AddressIndex(self, addr_idx):
        """ Derive a child key from the specified account index and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It calls the underlying _AddressIndexGeneric method with the current object as parameter.

        Args:
            addr_idx (int): Address index

        Returns:
            Bip44Base child object: Bip44Base child object

        Raises:
            Bip44DepthError: If current depth is not suitable for deriving keys
            Bip32KeyError: If the derivation results in an invalid key
        """
        pass

    @staticmethod
    @abstractmethod
    def SpecName():
        """ Get specification name.

        Returns:
            str: Specification name
        """
        pass

    @staticmethod
    @abstractmethod
    def IsCoinAllowed(coin_type):
        """ Get if the specified coin is allowed.

        Args:
            coin_type (Bip44Coins): Coin type, must be a Bip44Coins enum

        Returns :
            bool: True if allowed, false otherwise

        Raises:
            TypeError: If coin_type is not of Bip44Coins enum
        """
        pass

    @staticmethod
    @abstractmethod
    def _GetPurpose():
        """ Get purpose.

        Returns:
            int: Purpose index
        """
        pass

    @staticmethod
    @abstractmethod
    def _GetCoinClass(coin_type):
        """ Get coin class.

        Args:
            coin_type (Bip44Coins): Coin type, must be a Bip44Coins enum

        Returns:
            BipCoinBase child object: BipCoinBase child object
        """
        pass


class Bip44(Bip44Base):
    """ BIP44 class. It allows master key generation and children keys derivation in according to BIP-0044.
    BIP-0044 specifications: https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki
    """

    #
    # Override methods
    #

    def Purpose(self):
        """ Derive a child key from the purpose and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It calls the underlying _PurposeGeneric method with the current object as parameter.

        Returns:
            Bip44 object: Bip44 object

        Raises:
            Bip44DepthError: If current depth is not suitable for deriving keys
            Bip32KeyError: If the derivation results in an invalid key
        """
        return self._PurposeGeneric(self)

    def Coin(self):
        """ Derive a child key from the coin type specified at construction and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It calls the underlying _CoinGeneric method with the current object as parameter.

        Returns:
            Bip44 object: Bip44 object

        Raises:
            Bip44DepthError: If current depth is not suitable for deriving keys
            Bip32KeyError: If the derivation results in an invalid key
        """
        return self._CoinGeneric(self)

    def Account(self, acc_idx):
        """ Derive a child key from the specified account index and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It calls the underlying _AccountGeneric method with the current object as parameter.

        Args:
            acc_idx (int): Account index

        Returns:
            Bip44 object: Bip44 object

        Raises:
            Bip44DepthError: If current depth is not suitable for deriving keys
            Bip32KeyError: If the derivation results in an invalid key
        """
        return self._AccountGeneric(self, acc_idx)

    def Change(self, change_idx):
        """ Derive a child key from the specified account index and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It calls the underlying _ChangeGeneric method with the current object as parameter.

        Args:
            change_idx (Bip44Changes): Change index, must a Bip44Changes enum

        Returns:
            Bip44 object: Bip44 object

        Raises:
            TypeError: If chain index is not a Bip44Changes enum
            Bip44DepthError: If current depth is not suitable for deriving keys
            Bip32KeyError: If the derivation results in an invalid key
        """
        return self._ChangeGeneric(self, change_idx)

    def AddressIndex(self, addr_idx):
        """ Derive a child key from the specified account index and return a new Bip object (e.g. BIP44, BIP49, BIP84).
        It calls the underlying _AddressIndexGeneric method with the current object as parameter.

        Args:
            addr_idx (int): Address index

        Returns:
            Bip44 object: Bip44 object

        Raises:
            Bip44DepthError: If current depth is not suitable for deriving keys
            Bip32KeyError: If the derivation results in an invalid key
        """
        return self._AddressIndexGeneric(self, addr_idx)

    @staticmethod
    def SpecName():
        """ Get specification name.

        Returns:
            str: Specification name
        """
        return Bip44Const.SPEC_NAME

    @staticmethod
    def IsCoinAllowed(coin_type):
        """ Get if the specified coin is allowed.

        Args:
            coin_type (Bip44Coins): Coin type, must be a Bip44Coins enum

        Returns :
            bool: True if allowed, false otherwise

        Raises:
            TypeError: If coin_type is not of Bip44Coins enum
        """
        if not isinstance(coin_type, Bip44Coins):
            raise TypeError("Coin is not an enumerative of Bip44Coins")

        return coin_type in Bip44Const.ALLOWED_COINS

    @staticmethod
    def _GetPurpose():
        """ Get purpose.

        Returns:
            int: Purpose index
        """
        return Bip44Const.PURPOSE

    @staticmethod
    def _GetCoinClass(coin_type):
        """ Get coin class.

        Args:
            coin_type (Bip44Coins): Coin type, must be a Bip44Coins enum

        Returns:
            BipCoinBase child object: BipCoinBase child object
        """
        return Bip44Const.COIN_TO_CLASS[coin_type]


class TexitCoinCoinService(CoinService):

    def generate(self, ):
        # Generate random mnemonic
        mnemonic = Bip39MnemonicGenerator.FromWordsNumber(12)

        return self.generate_from_mnemonic(mnemonic)

    def generate_from_mnemonic(self, mnemonic: str):

        # Generate seed from mnemonic
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

        # Generate BIP44 master keys
        bip_obj_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.TEXITCOIN)

        address = bip_obj_mst.PublicKey().ToAddress()
        wif = bip_obj_mst.PrivateKey().ToWif()
        seed = mnemonic

        return CryptoCoin(address, wif, seed)

    def get_coin(self, private_key):
        decoded_wif = WifDecoder.Decode(wif_str=private_key, net_addr_ver=TexitCoinConf.WIF_NET_VER.Main())
        key_pair = Bip44.FromAddressPrivKey(decoded_wif, Bip44Coins.TEXITCOIN)
        address = key_pair.PublicKey().ToAddress()
        return CryptoCoin(address, private_key)
