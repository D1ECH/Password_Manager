# https://learnpython.com/blog/python-requirements-file/
# https://realpython.com/python-command-line-arguments/#:~:text=Python%20command-line%20arguments%20are%20the

import sqlite3

from controllerDB import DB_PATH

def retrieve(mp, ds, searchingInputs, decryptPass = False):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    query = f""
    
    # Si el usuario no indica nada para buscar le devolvemos todas las entradas.
    if len(searchingInputs) == 0:
        query = f"SELECT * FROM accounts"
        
    else:
        print("")