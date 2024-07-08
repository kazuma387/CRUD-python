from .conexion_db import ConexionDB2
from tkinter import messagebox

# Crear la tabla de representantes
def crear_tabla_representantes():
    conexion = ConexionDB2()
    sql = """
    CREATE TABLE representantes(
        id_representante INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_apellido VARCHAR(100),
        cedula VARCHAR(100),
        telefono VARCHAR(100),
        correo VARCHAR(100),
        direccion VARCHAR(100),
        serial_carnet VARCHAR(100),
        codigo_carnet VARCHAR(100)
    )
    """
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        messagebox.showinfo("Crear Registro", "Se creó la tabla de representantes en la base de datos")
    except Exception as e:
        messagebox.showwarning("Crear Registro", f"La tabla de representantes ya está creada en la base de datos. Error: {e}")

def borrar_tabla_representantes():
    conexion = ConexionDB2()
    sql = "DROP TABLE representantes"

    # Pedir confirmación al usuario
    respuesta = messagebox.askokcancel("Confirmación", "¿Está seguro de que desea borrar la tabla de representantes?")
    if respuesta:
        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
            messagebox.showinfo("Borrar Registro", "La tabla de representantes se borró con éxito")
        except Exception as e:
            messagebox.showerror("Borrar Registro", f"No hay ninguna tabla de representantes en la base de datos. Error: {e}")
    else:  # Si el usuario hizo clic en "Cancelar"
        messagebox.showinfo("Cancelar", "La operación de borrado se ha cancelado.")

# Clase Representante para la manipulación de datos
class Representante:
    def __init__(self, nombre_apellido, cedula, telefono, correo, direccion, serial_carnet, codigo_carnet):
        self.id_representante = None
        self.nombre_apellido = nombre_apellido
        self.cedula = cedula
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.serial_carnet = serial_carnet
        self.codigo_carnet = codigo_carnet

    def __str__(self):
        return f"Representante[{self.nombre_apellido}, {self.cedula}, {self.telefono}, {self.correo}, {self.direccion}, {self.serial_carnet}, {self.codigo_carnet}]"

# Funciones CRUD para Representantes
def guardar_representante(representante):
    conexion = ConexionDB2()
    sql = f"""INSERT INTO representantes (nombre_apellido, cedula, telefono, correo, direccion, serial_carnet, codigo_carnet)
            VALUES('{representante.nombre_apellido}', '{representante.cedula}', '{representante.telefono}', '{representante.correo}', 
            '{representante.direccion}', '{representante.serial_carnet}', '{representante.codigo_carnet}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as e:
        messagebox.showerror("Conexion al Registro", f"No hay ninguna tabla en la base de datos. Error: {e}")

def listar_representantes():
    conexion = ConexionDB2()

    representantes = []
    sql = "SELECT * FROM representantes"

    try:
        conexion.cursor.execute(sql)
        representantes = conexion.cursor.fetchall()
    except:
        titulo = "Conexion al Registro"
        mensaje = "Crea tabla representantes en la base de datos"
        # messagebox.showwarning(titulo, mensaje)
        print(mensaje)
    finally:
        conexion.cerrar()
    
    return representantes

def editar_representante(representante, id_representante):
    conexion = ConexionDB2()
    sql = f"""UPDATE representantes SET nombre_apellido = '{representante.nombre_apellido}', cedula ='{representante.cedula}', 
            telefono ='{representante.telefono}', correo = '{representante.correo}', direccion = '{representante.direccion}', 
            serial_carnet = '{representante.serial_carnet}', codigo_carnet = '{representante.codigo_carnet}'
            WHERE id_representante = '{id_representante}'"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as e:
        messagebox.showerror("Edición de datos", f"No se pudo editar el representante. Error: {e}")

def eliminar_representante(id_representante):
    conexion = ConexionDB2()
    sql = f"DELETE FROM representantes WHERE id_representante = {id_representante}"

    # Pedir confirmación al usuario
    respuesta = messagebox.askokcancel("Confirmación", "¿Está seguro de que desea borrar al representante?")
    if respuesta:
        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
            messagebox.showinfo("Eliminar datos", "Se eliminó el representante")
        except Exception as e:
            messagebox.showerror("Eliminar datos", f"No se pudo eliminar el representante. Error: {e}")
    else:  # Si el usuario hizo clic en "Cancelar"
        messagebox.showinfo("Cancelar", "La operación de borrado se ha cancelado.")

def consultar_representante(campo=None, valor=None):
    conexion = ConexionDB2()
    if campo and valor:
        sql = f"SELECT * FROM representantes WHERE {campo} = '{valor}'"
    else:
        sql = "SELECT * FROM representantes"
    try:
        conexion.cursor.execute(sql)
        representantes = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception as e:
        messagebox.showerror("Conexion al Registro", f"No se pudieron obtener los datos de los representantes. Error: {e}")
        return []
    return representantes