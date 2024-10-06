from getpass import getpass
from controllerDB import hash_password, DB_PATH
import sqlite3


def verify_master_password(hash_pass):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    query = f"SELECT masterPassword_hash FROM secrets"
    stored_hash = cursor.fetchone()[0]
    
    if(stored_hash == hash_pass):
        print("Contraseña correcta.")
        return True
    else:
        print("Contraseña incorrecta.")
        return False

    
def login():
    # Pedir la contraseña al usuario
    password = getpass("[+] Introduce tu contraseña maestra: ")
    verify_master_password(hash_password(password))