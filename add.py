import sqlite3
from getpass import getpass
from controllerDB import DB_PATH
from utils.encryption import encrypt_password
import entry_password

def add_entry(mp, ds):
    site_name = input("Introduce el nombre del sitio: ")
    site_url = input("Introduce la URL del sitio: ")
    email = input("Introduce el correo electrónico asociado (opcional): ")
    username = input("Introduce el nombre de usuario: ")
    password = entry_password.add_password(mp, ds)

    # encrypted_password = encrypt_password(password)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """INSERT INTO accounts (siteName, siteUrl, email, username, password) 
               VALUES (?, ?, ?, ?, ?)"""
    cursor.execute(query, (site_name, site_url, email, username, password))
    
    conn.commit()
    conn.close()

    print("Entrada añadida con éxito.")

if __name__ == "__main__":
    add_entry()