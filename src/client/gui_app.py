import tkinter as tk
from tkinter import ttk, messagebox
from model.estudiantes_dao import crear_tabla, borrar_tabla
from model.estudiantes_dao import Estudiante, guardar, listar, editar, eliminar, consultar

# creando barra de menu
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    # menu de inicio
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
    # opciones dentro del menu de inicio
    menu_inicio.add_command(label="Crear Registro en DB", command=crear_tabla)
    menu_inicio.add_command(label="Eliminar Registro en DB", command=borrar_tabla)
    menu_inicio.add_command(label="Salir", command=root.destroy)

# creando contenedor dentro de la ventana
# uso se clases para heredar comportamientos
class Frame(tk.Frame):
    #constructor
    def __init__(self, root=None):
        super().__init__(root, width=600, height=400)
        self.root = root
        self.pack()
        #self.config(bg="green")
        self.id_estudiante = None

        # para ejecutar la funcion
        self.estudiantes()
        self.desabilitar_campos()
        self.tabla_estudiantes()
    
    #datos de estudiantes
    def estudiantes(self):
        # labels de cada campo
        self.label_nombres_apellidos = tk.Label(self, text= "Nombres y Apellidos: ")
        self.label_nombres_apellidos.config(font=("Arial", 12, "bold"))
        # para posicionarlo en la ventana
        self.label_nombres_apellidos.grid(row=0, column=1, padx=1, pady=2)

        self.cedula = tk.Label(self, text= "Cédula: ")
        self.cedula.config(font=("Arial", 12, "bold"))
        self.cedula.grid(row=1, column=1, padx=1, pady=2)

        self.sexo = tk.Label(self, text= "Sexo: ")
        self.sexo.config(font=("Arial", 12, "bold"))
        self.sexo.grid(row=2, column=1, padx=1, pady=2)

        self.grado_seccion = tk.Label(self, text= "Grado y Sección: ")
        self.grado_seccion.config(font=("Arial", 12, "bold"))
        self.grado_seccion.grid(row=3, column=1, padx=1, pady=2)

        self.fecha_nacimiento = tk.Label(self, text= "Fecha de Nacimiento: ")
        self.fecha_nacimiento.config(font=("Arial", 12, "bold"))
        self.fecha_nacimiento.grid(row=4, column=1, padx=1, pady=2)

        self.lugar_nacimiento = tk.Label(self, text= "Lugar de Nacimiento: ")
        self.lugar_nacimiento.config(font=("Arial", 12, "bold"))
        self.lugar_nacimiento.grid(row=5, column=1, padx=1, pady=2)

        # Entrys Campos de entradas
        self.nombre_apellido = tk.StringVar()
        self.entry_nombre_apellido = tk.Entry(self, textvariable=self.nombre_apellido)
        self.entry_nombre_apellido.config(width=50, font=("Arial", 12))
        self.entry_nombre_apellido.grid(row=0, column=2, padx=1, pady=2, columnspan=2)
        
        self.cedula = tk.StringVar()
        self.entry_cedula = tk.Entry(self, textvariable=self.cedula)
        self.entry_cedula.config(width=50, font=("Arial", 12))
        self.entry_cedula.grid(row=1, column=2, padx=1, pady=2, columnspan=2)
        
        self.sexo = tk.StringVar()
        self.entry_sexo = tk.Entry(self, textvariable=self.sexo)
        self.entry_sexo.config(width=50, font=("Arial", 12))
        self.entry_sexo.grid(row=2, column=2, padx=1, pady=2, columnspan=2)
        
        self.grado_seccion = tk.StringVar()
        self.entry_grado_seccion = tk.Entry(self, textvariable=self.grado_seccion)
        self.entry_grado_seccion.config(width=50, font=("Arial", 12))
        self.entry_grado_seccion.grid(row=3, column=2, padx=1, pady=2, columnspan=2)
        
        self.fecha_nacimiento = tk.StringVar()
        self.entry_fecha_nacimiento = tk.Entry(self, textvariable=self.fecha_nacimiento)
        self.entry_fecha_nacimiento.config(width=50, font=("Arial", 12))
        self.entry_fecha_nacimiento.grid(row=4, column=2, padx=1, pady=2, columnspan=2)
        
        self.lugar_nacimiento = tk.StringVar()
        self.entry_lugar_nacimiento = tk.Entry(self, textvariable=self.lugar_nacimiento)
        self.entry_lugar_nacimiento.config(width=50, font=("Arial", 12))
        self.entry_lugar_nacimiento.grid(row=5, column=2, padx=1, pady=2, columnspan=2)

        # Botones
        # Nuevo
        self.boton_nuevo = tk.Button(self, text="Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(
            width=20, font=("Arial", 12, "bold"), fg="#DAD5D6",
            bg="#158645", cursor="hand2", activebackground="#35BD6F")
        self.boton_nuevo.grid(row=6, column=1, padx=1, pady=2)
        
        # Guardar
        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_campos)
        self.boton_guardar.config(
            width=20, font=("Arial", 12, "bold"), fg="#DAD5D6",
            bg="#1658A2", cursor="hand2", activebackground="#3586DF")
        self.boton_guardar.grid(row=6, column=2, padx=1, pady=2)

        # Cancelar
        self.boton_cancelar = tk.Button(self, text="Cancelar", command=self.desabilitar_campos)
        self.boton_cancelar.config(
            width=20, font=("Arial", 12, "bold"), fg="#DAD5D6",
            bg="#BD152E", cursor="hand2", activebackground="#E15370")
        self.boton_cancelar.grid(row=6, column=3, padx=1, pady=2)

    # Habilitar Campos
    def habilitar_campos(self):
        # para enviar datos vacios
        self.nombre_apellido.set("")
        self.cedula.set("")
        self.sexo.set("")
        self.grado_seccion.set("")
        self.fecha_nacimiento.set("")
        self.lugar_nacimiento.set("")

        self.entry_nombre_apellido.config(state="normal")
        self.entry_cedula.config(state="normal")
        self.entry_sexo.config(state="normal")
        self.entry_grado_seccion.config(state="normal")
        self.entry_fecha_nacimiento.config(state="normal")
        self.entry_lugar_nacimiento.config(state="normal")

        # Botones
        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")

    # desabilitar Campos
    def desabilitar_campos(self):
        self.id_estudiante = None
        # para enviar datos vacios
        self.nombre_apellido.set("")
        self.cedula.set("")
        self.sexo.set("")
        self.grado_seccion.set("")
        self.fecha_nacimiento.set("")
        self.lugar_nacimiento.set("")

        self.entry_nombre_apellido.config(state="disabled")
        self.entry_cedula.config(state="disabled")
        self.entry_sexo.config(state="disabled")
        self.entry_grado_seccion.config(state="disabled")
        self.entry_fecha_nacimiento.config(state="disabled")
        self.entry_lugar_nacimiento.config(state="disabled")

        # Botones
        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")
    
    # Guardar Campos
    def guardar_campos(self):

        estudiante = Estudiante(
            self.nombre_apellido.get(),
            self.cedula.get(),
            self.sexo.get(),
            self.grado_seccion.get(),
            self.fecha_nacimiento.get(),
            self.lugar_nacimiento.get(),
        )
        # para enviar
        if self.id_estudiante == None:
            guardar(estudiante)
        else:
            editar(estudiante, self.id_estudiante)

        #para actualizar la tabla al guardar
        self.tabla_estudiantes()

        # desabilitar campos
        self.desabilitar_campos()
    
    # mostrar tabla de Estudiantes anexados
    def tabla_estudiantes(self):
        # Recuperar lista de estudiantes
        self.lista_estudiantes = listar()
        self.lista_estudiantes.reverse()

        self.tabla = ttk.Treeview(self, 
            columns=("Nombres y Apellidos", "Cédula", "Sexo",
            "Grado y Seccion", "Fecha de Nacimiento", "Lugar de Nacimiento"))
        self.tabla.grid(row=7, columnspan=6, sticky='nse')

        # scrollbar para la tabla cuando posea muchos registros
        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.scroll.grid(row=7, columnspan=7, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        # Encabezado de la tabla
        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Nombres y Apellidos")
        self.tabla.heading("#2", text="Cédula")
        self.tabla.heading("#3", text="Sexo")
        self.tabla.heading("#4", text="Grado y Sección")
        self.tabla.heading("#5", text="Fecha de Nacimiento")
        self.tabla.heading("#6", text="Lugar de Nacimiento")

        # iterar lista de estudiantes
        for e in self.lista_estudiantes:
            self.tabla.insert('', 0, text=e[0], values=(e[1], e[2], e[3], e[4], e[5], e[6]))

        # Botones
        # Editar
        self.boton_editar = tk.Button(self, text="Editar", command=self.editar_datos)
        self.boton_editar.config(
            width=20, font=("Arial", 12, "bold"), fg="#DAD5D6",
            bg="#158645", cursor="hand2", activebackground="#35BD6F")
        self.boton_editar.grid(row=8, column=1, padx=1, pady=2)

        # Eliminar
        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_datos)
        self.boton_eliminar.config(
            width=20, font=("Arial", 12, "bold"), fg="#DAD5D6",
            bg="#BD152E", cursor="hand2", activebackground="#E15370")
        self.boton_eliminar.grid(row=8, column=2, padx=1, pady=2)

        # Consultar
        self.boton_consultar = tk.Button(self, text="Consultar", command=self.consultar_datos)
        self.boton_consultar.config(
            width=20, font=("Arial", 12, "bold"), fg="#DAD5D6",
            bg="#1658A2", cursor="hand2", activebackground="#3586DF")
        self.boton_consultar.grid(row=8, column=3, padx=1, pady=2)
    
    # repuperando para editar el valor seccionado de la tabla
    def editar_datos(self):
        try:
            self.id_estudiante = self.tabla.item(self.tabla.selection())['text']
            self.nombre_apellido_estudiante = self.tabla.item(self.tabla.selection())['values'][0]
            self.cedula_estudiante = self.tabla.item(self.tabla.selection())['values'][1]
            self.sexo_estudiante = self.tabla.item(self.tabla.selection())['values'][2]
            self.grado_seccion_estudiante = self.tabla.item(self.tabla.selection())['values'][3]
            self.fecha_nacimiento_estudiante = self.tabla.item(self.tabla.selection())['values'][4]
            self.lugar_nacimiento_estudiante = self.tabla.item(self.tabla.selection())['values'][5]

            self.habilitar_campos()

            self.entry_nombre_apellido.insert(0, self.nombre_apellido_estudiante)
            self.entry_cedula.insert(1, self.cedula_estudiante)
            self.entry_sexo.insert(2, self.sexo_estudiante)
            self.entry_grado_seccion.insert(3, self.grado_seccion_estudiante)
            self.entry_fecha_nacimiento.insert(4, self.fecha_nacimiento_estudiante)
            self.entry_lugar_nacimiento.insert(5, self.lugar_nacimiento_estudiante)
        except:
            titulo = "Edición de datos"
            mensaje = "No se ha seleccionado ningun registro"
            messagebox.showerror(titulo, mensaje)
    
    # para eliminar un dato seleccionado de la tabla
    def eliminar_datos(self):
        try:
            self.id_estudiante = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_estudiante)
            # para que se actualize
            self.tabla_estudiantes()
            self.id_estudiante = None
        except:
            titulo = "Eliminar de datos"
            mensaje = "No se ha seleccionado ningun registro"
            messagebox.showerror(titulo, mensaje)

    # para buscar un estudiante en la BD mediante nombre, id, o cedula
    def consultar_datos(self):
        def consultar_por_campo(campo, valor):
            estudiantes = consultar(campo=campo, valor=valor)
            if estudiantes:
                self.lista_estudiantes = estudiantes
                self.tabla_estudiantes()
                self.id_estudiante = None
            
                # Mostrar resultados en la ventana emergente
                resultado_text.delete(1.0, tk.END)
                for estudiante in estudiantes:
                    resultado_text.insert(tk.END, f"ID: {estudiante[0]}\n")
                    resultado_text.insert(tk.END, f"Nombre y Apellido: {estudiante[1]}\n")
                    resultado_text.insert(tk.END, f"Cédula: {estudiante[2]}\n")
                    resultado_text.insert(tk.END, f"Sexo: {estudiante[3]}\n")
                    resultado_text.insert(tk.END, f"Grado y Sección: {estudiante[4]}\n")
                    resultado_text.insert(tk.END, f"Fecha de Nacimiento: {estudiante[5]}\n")
                    resultado_text.insert(tk.END, f"Lugar de Nacimiento: {estudiante[6]}\n")
                    resultado_text.insert(tk.END, "\n")
            else:
                titulo = "Consulta de datos"
                mensaje = "No se ha encontrado el registro"
                messagebox.showerror(titulo, mensaje)
        
        def limpiar_consulta():
            entry_valor.delete(0, tk.END)
            resultado_text.delete(1.0, tk.END)
    
        # Crear una ventana emergente para ingresar los datos de búsqueda
        ventana_consultar = tk.Toplevel(self)
        ventana_consultar.title("Consultar Estudiante")
        ventana_consultar.iconbitmap("C:/Users/pc/Documents/Python/CRUD tkinter sqlite/src/img/lupa.ico")

        label_consultar_por = tk.Label(ventana_consultar, text="Consultar por:")
        label_consultar_por.grid(row=0, column=0)

        option_consultar_por = tk.StringVar()
        option_consultar_por.set("id_estudiante")
        opciones_consultar_por = ["id_estudiante", "nombre_apellido", "cedula"]
        for i, opcion in enumerate(opciones_consultar_por):
            tk.Radiobutton(ventana_consultar, text=opcion, variable=option_consultar_por, value=opcion).grid(row=0, column=i+1)

        label_valor = tk.Label(ventana_consultar, text="Valor:")
        label_valor.grid(row=1, column=0)

        entry_valor = tk.Entry(ventana_consultar)
        entry_valor.grid(row=1, column=1)

        boton_consultar = tk.Button(ventana_consultar, text="Consultar", command=lambda: consultar_por_campo(option_consultar_por.get(), entry_valor.get()))
        boton_consultar.grid(row=2, column=0, columnspan=2)

        # "Limpiar Consulta" que eliminará el valor ingresado en el campo de búsqueda 
        # y limpiará el área de texto que muestra los resultados de la consulta.
        boton_limpiar = tk.Button(ventana_consultar, text="Limpiar Consulta", command=lambda: limpiar_consulta())
        boton_limpiar.grid(row=2, column=2, columnspan=2)

        # Agregar un widget de texto para mostrar los resultados
        resultado_text = tk.Text(ventana_consultar, height=10, width=50)
        resultado_text.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

        ventana_consultar.mainloop()