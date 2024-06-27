import sqlite3

# para conectar al la base de datos y sino exite crear una
class ConexionDB:
    # abrir la conexion
    def __init__(self):
        self.base_datos = "database/estudiantes.db"
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()
    
    # cerrar la conexion
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()