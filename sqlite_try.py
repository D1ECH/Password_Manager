import sqlite3

def createDB():
    conn = sqlite3.connect("password_manager.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE password_manager.db(
            name text
                 
        )"""
    )
    conn.commit()
    conn.close()
    
def insertRow():
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    
    instruction = f"INSERT INTO password_manager VALUES ()"
    
    cursor.execute(instruction)
    conn.commit()
    conn.close()

"""
Lo que conseguimos con esto es que a la hora de importar este archivo en otro, todo lo
que está contenido en el main no se va a ejecutar, así simplemente importamos las funciones
definidas y el main nos sirve para ejecutar el archivo en cuestión, pero desde cualquier
otro es invisible.
"""
if __name__ == "__main__":
    createDB()