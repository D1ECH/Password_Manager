from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from utils import encryption

def compute_MK(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key = PBKDF2(password, salt, 32, 1000000, hmac_hash_module=SHA512)
    return key

def add_password(mp, ds):
    password = getpass("Introduce la contraseña: ")
    
    # Computar Master_Key 
    mk = compute_MK(mp, ds)
    encrypted = encryption.encrypt(mk, password, "bytes")