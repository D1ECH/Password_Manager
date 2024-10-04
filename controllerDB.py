######################################################################################################
# IMPORTS
######################################################################################################

from getpass import getpass
import hashlib
import random
import sqlite3 as sql
import string
import random
######################################################################################################
######################################################################################################



######################################################################################################
# VARIABLES GLOBALES
######################################################################################################
db = "password_manager.db"
######################################################################################################
######################################################################################################



######################################################################################################
# MÉTODOS Y FUNCIONES
######################################################################################################
def createDB(db):
    try:
        conn = sql.connect(db)
    
    except sql.Error:
        print("Error open db.\n")
        return False
    conn.commit()
    conn.close()
######################################################################################################    
def createTables(db):
    conn = sql.connect(db)
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
# def insertRow(db):
#     conn = sql.connect(db)
#     cursor = conn.cursor()
    
#     instruction = f"INSERT INTO password_manager VALUES ('diego', 'google.com')"
    
#     cursor.execute(instruction)
#     conn.commit()
#     conn.close()
######################################################################################################

def masterPassword():
    while 1:
        mp = getpass("¿Cuál va a ser tu contraseña maestra? --> ")
        if mp==getpass("Repite la contraseña --> ") and mp!="":
            break
        print("Please try again")
    # Hashing Master Password
    hashed_mp = hashlib.sha512(mp.encode()).hexdigest()
    print("Generated hash of Master Password")
    return hashed_mp

######################################################################################################

def deviceSecretGenerator(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

######################################################################################################

def secrets2DB(db):
    conn = sql.connect(db)
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
    createDB(db)
    createTables(db)
    secrets2DB(db)
######################################################################################################
######################################################################################################    
