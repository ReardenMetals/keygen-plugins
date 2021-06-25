# encoding: utf-8
# module ed25519._ed25519
# from C:\Users\Boday Alfaro\PycharmProjects\cardanoProject1\venv\lib\site-packages\ed25519\_ed25519.cp36-win_amd64.pyd
# by generator 1.147
""" Low-level Ed25519 signature/verification functions. """
# no imports

# Variables with simple values

PUBLICKEYBYTES = 32

SECRETKEYBYTES = 64

SIGNATUREKEYBYTES = 64

# functions

def open(message, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    open(message+signature, verifying_key)
    
    Check the signature for validity. Returns the message if valid, raises
    ed25519.error if not.
    """
    pass

def publickey(signkey_seed): # real signature unknown; restored from __doc__
    """
    publickey(signkey_seed)
    
    Accepts a 32-byte seed. Return a tuple of (verfkey, signkey), with the
    64-byte private signing key and the corresponding 32-byte public
    verfiying key.
    """
    pass

def sign(message, signing_key): # real signature unknown; restored from __doc__
    """
    sign(message, signing_key)
    
    Return the concatenation of three parts: the 32-byte R signature value,
    the 32-byte S signature value, and the original message.
    """
    pass

# classes

class BadSignatureError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022F68B4C128>'

__spec__ = None # (!) real value is "ModuleSpec(name='ed25519._ed25519', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022F68B4C128>, origin='C:\\\\Users\\\\Boday Alfaro\\\\PycharmProjects\\\\cardanoProject1\\\\venv\\\\lib\\\\site-packages\\\\ed25519\\\\_ed25519.cp36-win_amd64.pyd')"

