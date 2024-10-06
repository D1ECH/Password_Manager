######################################################################################################
# IMPORTS
######################################################################################################

from getpass import getpass
import hashlib
import random
import sqlite3 as sql
import string
import random
from pathlib import Path

######################################################################################################
######################################################################################################



######################################################################################################
# VARIABLES GLOBALES
######################################################################################################
DB_NAME = "password_manager.db"

# Ruta base del directorio actual
BASE_DIR = Path(__file__).resolve().parent
# Ruta de la carpeta 'db'
DB_FOLDER = BASE_DIR / 'db'
# Ruta completa del archivo de la base de datos
DB_PATH = DB_FOLDER / DB_NAME
######################################################################################################
######################################################################################################



######################################################################################################
# MÉTODOS Y FUNCIONES
######################################################################################################
def createDB(DB_PATH):
    try:
        conn = sql.connect(DB_PATH)
    
    except sql.Error:
        print("Error open db.\n")
        return False
    conn.commit()
    conn.close()
######################################################################################################    
def createTables(DB_PATH):
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    
    query = """CREATE TABLE IF NOT EXISTS secrets (
        masterPassword_hash text not null,
        device_secret text not null     
    )"""
    
    cursor.execute(query)
    
    query = """CREATE TABLE IF NOT EXISTS accounts (
        siteName text not null,
        siteUrl text not null,
        email text,
        usermane text,
        password text not null     
    )"""
    
    cursor.execute(query)
    
    conn.commit()
    conn.close()

######################################################################################################
# def insertRow(DB_PATH):
#     conn = sql.connect(DB_PATH)
#     cursor = conn.cursor()
    
#     instruction = f"INSERT INTO password_manager VALUES ('diego', 'google.com')"
    
#     cursor.execute(instruction)
#     conn.commit()
#     conn.close()
######################################################################################################
def hash_password(mp):
    return hashlib.sha512(mp.encode()).hexdigest()
######################################################################################################
def masterPassword():
    while 1:
        mp = getpass("¿Cuál va a ser tu contraseña maestra? --> ")
        if mp==getpass("Repite la contraseña --> ") and mp!="":
            break
        print("Please try again")
    # Hashing Master Password
    hashed_mp = hash_password(mp)
    print("Generated hash of Master Password")
    return hashed_mp

######################################################################################################

def deviceSecretGenerator(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

######################################################################################################

def secrets2DB(DB_PATH):
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    
    ds = deviceSecretGenerator(16)
    hashed_mp = masterPassword()
    
    # Consulta SQL con placeholders para los valores
    query = "INSERT INTO secrets (masterPassword_hash, device_secret) VALUES (?, ?)"

    # Ejecutar la consulta con los valores
    cursor.execute(query, (hashed_mp, ds))
    
    conn.commit()
    conn.close()
    
######################################################################################################
######################################################################################################



######################################################################################################
# MAIN
######################################################################################################
if __name__ == "__main__":
    createDB(DB_PATH)
    createTables(DB_PATH)
    secrets2DB(DB_PATH)
######################################################################################################
######################################################################################################    
