from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    # crea la conexion
    conexion = ConexionDB()

    # crea la tabla
    sql = """
    CREATE TABLE estudiantes(
        id_estudiante INTEGER,
        nombre_apellido VARCHAR(100),
        cedula varchar(100),
        sexo VARCHAR(100),
        grado_seccion VARCHAR(100),
        fecha_nacimiento VARCHAR(100),
        lugar_nacimiento VARCHAR(100),
        PRIMARY KEY(id_estudiante AUTOINCREMENT)
    )
    """

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Crear Registro"
        mensaje = "Se creó la tabla en la base de datos"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Crear Registro"
        mensaje = "La tabla ya esta creada en la base de datos"
        messagebox.showwarning(titulo, mensaje)
    

def borrar_tabla():
    conexion = ConexionDB()

    sql = "DROP TABLE estudiantes"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Borrar Registro"
        mensaje = "La tabla en la base de datos se borro con éxito"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Borrar Registro"
        mensaje = "No hay ninguna tabla en la base de datos"
        messagebox.showerror(titulo, mensaje)

class Estudiante:
    def __init__(self, nombre_apellido, cedula,
    sexo, grado_seccion, fecha_nacimiento, lugar_nacimiento):
        self.id_estudiante = None
        self.nombre_apellido = nombre_apellido
        self.cedula = cedula
        self.sexo = sexo
        self.grado_seccion = grado_seccion
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
    
    # ver el estado del objeto
    def __str__(self):
        return f"Estudiante[{self.nombre_apellido}, {self.cedula}, {self.sexo}, {self.grado_seccion}, {self.fecha_nacimiento}, {self.lugar_nacimiento}]"
    
# para guardar en DB
def guardar(estudiante):
    conexion = ConexionDB()

    sql = f"""INSERT INTO estudiantes (nombre_apellido, cedula,
sexo, grado_seccion, fecha_nacimiento, lugar_nacimiento)
VALUES('{estudiante.nombre_apellido}', '{estudiante.cedula}', '{estudiante.sexo}',
'{estudiante.grado_seccion}', '{estudiante.fecha_nacimiento}', '{estudiante.lugar_nacimiento}')"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Conexion al Registro"
        mensaje = "No hay ninguna tabla en la base de datos"
        messagebox.showerror(titulo, mensaje)

# para listar lo que insertamos en la tabla
def listar():
    conexion = ConexionDB()

    lista_estudiantes = []
    sql = "SELECT * FROM estudiantes"

    try:
        conexion.cursor.execute(sql)
        lista_estudiantes = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = "Conexion al Registro"
        mensaje = "Crea tabla en la base de datos"
        messagebox.showwarning(titulo, mensaje)
    
    return lista_estudiantes

# para editar contenido en la tabla
def editar(estudiante, id_estudiante):
    conexion = ConexionDB()

    sql = f"""UPDATE estudiantes
    SET nombre_apellido = '{estudiante.nombre_apellido}', cedula ='{estudiante.cedula}', 
    sexo ='{estudiante.sexo}', grado_seccion = '{estudiante.grado_seccion}', 
    fecha_nacimiento = '{estudiante.fecha_nacimiento}', lugar_nacimiento = '{estudiante.lugar_nacimiento}'
    WHERE id_estudiante = '{id_estudiante}'"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Edición de datos"
        mensaje = "No se ha podido editar este dato"
        messagebox.showerror(titulo, mensaje)

# para eliminar contenido de la tabla
def eliminar(id_estudiante):
    conexion = ConexionDB()

    sql = f"DELETE FROM estudiantes WHERE id_estudiante = {id_estudiante}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Eliminar de datos"
        mensaje = "Se ha eliminado el registro"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Eliminar datos"
        mensaje = "No se ha seleccionado ningun registro"
        messagebox.showerror(titulo, mensaje)

# para consultar un estudiante
def consultar(campo=None, valor=None):
    conexion = ConexionDB()

    if campo and valor:
        sql = f"SELECT * FROM estudiantes WHERE {campo} = '{valor}'"
    else:
        sql = "SELECT * FROM estudiantes"

    try:
        conexion.cursor.execute(sql)
        estudiantes = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = "Conexion al Registro"
        mensaje = "No se pudo obtener los datos de la base de datos"
        messagebox.showerror(titulo, mensaje)
        return []

    return estudiantes