import tkinter as tk
from tkinter import ttk, messagebox
from model.representantes import Representante, guardar_representante, listar_representantes, editar_representante, eliminar_representante, consultar_representante

    # creando contenedor dentro de la ventana
# uso se clases para heredar comportamientos
class Frame_representantes(tk.Frame):
    #constructor
    def __init__(self, root=None):
        super().__init__(root, width=600, height=400)
        self.root = root
        self.pack()
        self.id_representante = None

        # para ejecutar la funcion
        self.representantes()
        self.desabilitar_campos_representantes()
        self.tabla_representantes()

    # Datos representantes
    def representantes(self):
        # labels de cada campo
        self.label_nombres_apellidos = tk.Label(self, text= "Nombres y Apellidos: ")
        self.label_nombres_apellidos.config(font=("Arial", 12, "bold"))
        # para posicionarlo en la ventana
        self.label_nombres_apellidos.grid(row=0, column=1, padx=1, pady=2)

        self.cedula = tk.Label(self, text= "Cédula: ")
        self.cedula.config(font=("Arial", 12, "bold"))
        self.cedula.grid(row=1, column=1, padx=1, pady=2)

        self.telefono = tk.Label(self, text= "Teléfono: ")
        self.telefono.config(font=("Arial", 12, "bold"))
        self.telefono.grid(row=2, column=1, padx=1, pady=2)

        self.correo = tk.Label(self, text= "Correo: ")
        self.correo.config(font=("Arial", 12, "bold"))
        self.correo.grid(row=3, column=1, padx=1, pady=2)

        self.direccion = tk.Label(self, text= "Dirección: ")
        self.direccion.config(font=("Arial", 12, "bold"))
        self.direccion.grid(row=4, column=1, padx=1, pady=2)

        self.serial_carnet = tk.Label(self, text= "Serial del Carnet: ")
        self.serial_carnet.config(font=("Arial", 12, "bold"))
        self.serial_carnet.grid(row=5, column=1, padx=1, pady=2)

        self.Codigo_carnet = tk.Label(self, text= "Código del Carnet: ")
        self.Codigo_carnet.config(font=("Arial", 12, "bold"))
        self.Codigo_carnet.grid(row=6, column=1, padx=1, pady=2)

        # Entrys Campos de entradas
        self.nombre_apellido = tk.StringVar()
        self.entry_nombre_apellido = tk.Entry(self, textvariable=self.nombre_apellido)
        self.entry_nombre_apellido.config(width=50, font=("Arial", 12))
        self.entry_nombre_apellido.grid(row=0, column=2, padx=1, pady=2, columnspan=2)
        
        self.cedula = tk.StringVar()
        self.entry_cedula = tk.Entry(self, textvariable=self.cedula)
        self.entry_cedula.config(width=50, font=("Arial", 12))
        self.entry_cedula.grid(row=1, column=2, padx=1, pady=2, columnspan=2)
        
        self.telefono = tk.StringVar()
        self.entry_telefono = tk.Entry(self, textvariable=self.telefono)
        self.entry_telefono.config(width=50, font=("Arial", 12))
        self.entry_telefono.grid(row=2, column=2, padx=1, pady=2, columnspan=2)
        
        self.correo = tk.StringVar()
        self.entry_correo = tk.Entry(self, textvariable=self.correo)
        self.entry_correo.config(width=50, font=("Arial", 12))
        self.entry_correo.grid(row=3, column=2, padx=1, pady=2, columnspan=2)
        
        self.direccion = tk.StringVar()
        self.entry_direccion = tk.Entry(self, textvariable=self.direccion)
        self.entry_direccion.config(width=50, font=("Arial", 12))
        self.entry_direccion.grid(row=4, column=2, padx=1, pady=2, columnspan=2)
        
        self.serial_carnet = tk.StringVar()
        self.entry_serial_carnet = tk.Entry(self, textvariable=self.serial_carnet)
        self.entry_serial_carnet.config(width=50, font=("Arial", 12))
        self.entry_serial_carnet.grid(row=5, column=2, padx=1, pady=2, columnspan=2)

        self.codigo_carnet = tk.StringVar()
        self.entry_codigo_carnet = tk.Entry(self, textvariable=self.codigo_carnet)
        self.entry_codigo_carnet.config(width=50, font=("Arial", 12))
        self.entry_codigo_carnet.grid(row=6, column=2, padx=1, pady=2, columnspan=2)

        # Botones
        # Nuevo
        self.boton_nuevo = tk.Button(self, text="Nuevo", command=self.habilitar_campos_representantes)
        self.boton_nuevo.config(
            width=20, font=("Arial", 12, "bold"), fg="#DAD5D6",
            bg="#158645", cursor="hand2", activebackground="#35BD6F")
        self.boton_nuevo.grid(row=7, column=1, padx=1, pady=2)
        
        # Guardar
        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_campos_representantes)
        self.boton_guardar.config(
            width=20, font=("Arial", 12, "bold"), fg="#DAD5D6",
            bg="#1658A2", cursor="hand2", activebackground="#3586DF")
        self.boton_guardar.grid(row=7, column=2, padx=1, pady=2)

        # Cancelar
        self.boton_cancelar = tk.Button(self, text="Cancelar", command=self.desabilitar_campos_representantes)
        self.boton_cancelar.config(
            width=20, font=("Arial", 12, "bold"), fg="#DAD5D6",
            bg="#BD152E", cursor="hand2", activebackground="#E15370")
        self.boton_cancelar.grid(row=7, column=3, padx=1, pady=2)
    
    # Habilitar Campos
    def habilitar_campos_representantes(self):
        # para enviar datos vacios
        self.nombre_apellido.set("")
        self.cedula.set("")
        self.telefono.set("")
        self.correo.set("")
        self.direccion.set("")
        self.serial_carnet.set("")
        self.codigo_carnet.set("")

        self.entry_nombre_apellido.config(state="normal")
        self.entry_cedula.config(state="normal")
        self.entry_telefono.config(state="normal")
        self.entry_correo.config(state="normal")
        self.entry_direccion.config(state="normal")
        self.entry_serial_carnet.config(state="normal")
        self.entry_codigo_carnet.config(state="normal")

        # Botones
        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")
    
    # desabilitar Campos
    def desabilitar_campos_representantes(self):
        self.id_representante = None
        # para enviar datos vacios
        self.nombre_apellido.set("")
        self.cedula.set("")
        self.telefono.set("")
        self.correo.set("")
        self.direccion.set("")
        self.serial_carnet.set("")
        self.codigo_carnet.set("")

        self.entry_nombre_apellido.config(state="disabled")
        self.entry_cedula.config(state="disabled")
        self.entry_telefono.config(state="disabled")
        self.entry_correo.config(state="disabled")
        self.entry_direccion.config(state="disabled")
        self.entry_serial_carnet.config(state="disabled")
        self.entry_codigo_carnet.config(state="disabled")

        # Botones
        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")
    
    # Guardar Campos
    def guardar_campos_representantes(self):

        representante = Representante(
            self.nombre_apellido.get(),
            self.cedula.get(),
            self.telefono.get(),
            self.correo.get(),
            self.direccion.get(),
            self.serial_carnet.get(),
            self.codigo_carnet.get(),
        )
        # para enviar
        if self.id_representante == None:
            guardar_representante(representante)
        else:
            editar_representante(representante, self.id_representante)

        #para actualizar la tabla al guardar
        self.tabla_representantes()

        # desabilitar campos
        self.desabilitar_campos_representantes()
    
    def actualizar_tabla_representantes(self):
        # Borrar todas las filas de la tabla
        self.tabla.delete(*self.tabla.get_children())
        
        # Obtener la lista actualizada de estudiantes desde la base de datos
        self.lista_representantes = listar_representantes()
        self.lista_representantes.reverse()
        
        # Insertar los datos actualizados en la tabla
        for e in self.lista_representantes:
            self.tabla.insert('', 0, text=e[0], values=(e[1], e[2], e[3], e[4], e[5], e[6]))

    # mostrar tabla de Estudiantes anexados
    def tabla_representantes(self):
        # Recuperar lista de estudiantes
        self.lista_representantes = listar_representantes()
        self.lista_representantes.reverse()

        # Crear tabla
        self.tabla = ttk.Treeview(self, 
            columns=("Nombres y Apellidos", "Cédula", "Telefono",
            "Correo", "Dirección", "Serial del Carnet", "Código del Carnet"))
        self.tabla.grid(row=8, columnspan=6, sticky='nse')

        # Crear scrollbar vertical
        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.scroll.grid(row=8, columnspan=8, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        # Encabezado de la tabla
        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Nombres y Apellidos")
        self.tabla.heading("#2", text="Cédula")
        self.tabla.heading("#3", text="Telefono")
        self.tabla.heading("#4", text="Correo")
        self.tabla.heading("#5", text="Dirección")
        self.tabla.heading("#6", text="Serial del Carnet")
        self.tabla.heading("#7", text="Código del Carnet")

        # Ajustar el ancho de las columnas
        self.tabla.column("#0", width=50)  # ID
        self.tabla.column("#1", width=200, anchor="center")  # Nombres y Apellidos
        self.tabla.column("#2", width=100, anchor="center")  # Cédula
        self.tabla.column("#3", width=100, anchor="center")  # Telefono
        self.tabla.column("#4", width=150, anchor="center")  # Correo
        self.tabla.column("#5", width=150, anchor="center")  # Dirección
        self.tabla.column("#6", width=100, anchor="center")  # Serial carnet de la patria
        self.tabla.column("#7", width=100, anchor="center")  # Código carnet de la patria

        # iterar lista de representantes
        for e in self.lista_representantes:
            self.tabla.insert('', 0, text=e[0], values=(e[1], e[2], e[3], e[4], e[5], e[6], e[7]))

        # Botones
        # Editar
        self.boton_editar = tk.Button(self, text="Editar", command=self.editar_datos_representante)
        self.boton_editar.config(
            width=20, font=("Arial", 12, "bold"), fg="#DAD5D6",
            bg="#158645", cursor="hand2", activebackground="#35BD6F")
        self.boton_editar.grid(row=9, column=1, padx=1, pady=2)

        # Eliminar
        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_datos_representante)
        self.boton_eliminar.config(
            width=20, font=("Arial", 12, "bold"), fg="#DAD5D6",
            bg="#BD152E", cursor="hand2", activebackground="#E15370")
        self.boton_eliminar.grid(row=9, column=2, padx=1, pady=2)

        # Consultar
        self.boton_consultar = tk.Button(self, text="Consultar", command=self.consultar_datos_representante)
        self.boton_consultar.config(
            width=20, font=("Arial", 12, "bold"), fg="#DAD5D6",
            bg="#1658A2", cursor="hand2", activebackground="#3586DF")
        self.boton_consultar.grid(row=9, column=3, padx=1, pady=2)

    # repuperando para editar el valor seccionado de la tabla
    def editar_datos_representante(self):
        try:
            self.id_representante = self.tabla.item(self.tabla.selection())['text']
            self.nombre_apellido_representante = self.tabla.item(self.tabla.selection())['values'][0]
            self.cedula_representante = self.tabla.item(self.tabla.selection())['values'][1]
            self.telefono_representante = self.tabla.item(self.tabla.selection())['values'][2]
            self.correo_representante = self.tabla.item(self.tabla.selection())['values'][3]
            self.direccion_representante = self.tabla.item(self.tabla.selection())['values'][4]
            self.serial_carnet_representante = self.tabla.item(self.tabla.selection())['values'][5]
            self.codigo_carnet_representante = self.tabla.item(self.tabla.selection())['values'][6]

            self.habilitar_campos_representantes()

            self.entry_nombre_apellido.insert(0, self.nombre_apellido_representante)
            self.entry_cedula.insert(1, self.cedula_representante)
            self.entry_telefono.insert(2, self.telefono_representante)
            self.entry_correo.insert(3, self.correo_representante)
            self.entry_direccion.insert(4, self.direccion_representante)
            self.entry_serial_carnet.insert(5, self.serial_carnet_representante)
            self.entry_codigo_carnet.insert(6, self.codigo_carnet_representante)

        except:
            titulo = "Edición de datos"
            mensaje = "No se ha seleccionado ningun registro"
            messagebox.showerror(titulo, mensaje)
    
    # para eliminar un dato seleccionado de la tabla
    def eliminar_datos_representante(self):
        self.id_representante = self.tabla.item(self.tabla.selection())['text']
        if self.id_representante:
            eliminar_representante(self.id_representante)
            # para que se actualize
            self.tabla_representantes()
            self.id_representante = None
        else:
            titulo = "Eliminar de datos"
            mensaje = "No se ha seleccionado ningun registro"
            messagebox.showerror(titulo, mensaje)

    # para buscar un representante en la BD mediante nombre, id, o cedula
    def consultar_datos_representante(self):
        def consultar_por_campo(campo, valor):
            representantes = consultar_representante(campo=campo, valor=valor)
            if representantes:
                self.lista_representantes = representantes
                self.tabla_representantes()
                self.id_representante = None
            
                # Mostrar resultados en la ventana emergente
                resultado_text.delete(1.0, tk.END)
                for representante in representantes:
                    resultado_text.insert(tk.END, f"ID: {representante[0]}\n")
                    resultado_text.insert(tk.END, f"Nombre y Apellido: {representante[1]}\n")
                    resultado_text.insert(tk.END, f"Cédula: {representante[2]}\n")
                    resultado_text.insert(tk.END, f"Teléfono: {representante[3]}\n")
                    resultado_text.insert(tk.END, f"Correo: {representante[4]}\n")
                    resultado_text.insert(tk.END, f"Dirección: {representante[5]}\n")
                    resultado_text.insert(tk.END, f"Serial del Carnet: {representante[6]}\n")
                    resultado_text.insert(tk.END, f"Código del Carnet: {representante[7]}\n")
                    resultado_text.insert(tk.END, "\n")
            else:
                titulo = "Consulta de datos"
                mensaje = "No se ha encontrado el registro"
                messagebox.showerror(titulo, mensaje)
        
        def limpiar_consulta():
            entry_valor.delete(0, tk.END)
            resultado_text.delete(1.0, tk.END)
        
        # para editar el representante en la consulta
        def editar_datos_consulta_representante():
            seleccion = resultado_text.tag_ranges(tk.SEL)
            if seleccion:
                contenido = resultado_text.get(seleccion[0], seleccion[1])
                lineas = contenido.split('\n')
                representante = {}
                for linea in lineas:
                    if ':' in linea:
                        clave, valor = linea.split(':', 1)
                        representante[clave.strip()] = valor.strip()
                
                if 'ID' in representante:
                    self.habilitar_campos_representantes()
                    self.id_representante = representante['ID']
                    self.entry_nombre_apellido.delete(0, tk.END)
                    self.entry_nombre_apellido.insert(0, representante.get('Nombre y Apellido', ''))
                    self.entry_cedula.delete(0, tk.END)
                    self.entry_cedula.insert(0, representante.get('Cédula', ''))
                    self.entry_telefono.delete(0, tk.END)
                    self.entry_telefono.insert(0, representante.get('Teléfono', ''))
                    self.entry_correo.delete(0, tk.END)
                    self.entry_correo.insert(0, representante.get('Correo', ''))
                    self.entry_direccion.delete(0, tk.END)
                    self.entry_direccion.insert(0, representante.get('Dirección', ''))
                    self.entry_serial_carnet.delete(0, tk.END)
                    self.entry_serial_carnet.insert(0, representante.get('Serial del Carnet', ''))
                    self.entry_codigo_carnet.delete(0, tk.END)
                    self.entry_codigo_carnet.insert(0, representante.get('Código del Carnet', ''))
                    
                    ventana_consultar.destroy()
                else:
                    messagebox.showerror("Error", "Por favor, seleccione un representante completo")
            else:
                messagebox.showerror("Error", "No se ha seleccionado ningún representante")

        # para eliminar el representante en la consulta
        def eliminar_datos_consulta_representante():
            seleccion = resultado_text.tag_ranges(tk.SEL)
            if seleccion:
                contenido = resultado_text.get(seleccion[0], seleccion[1])
                lineas = contenido.split('\n')
                representante = {}
                for linea in lineas:
                    if ':' in linea:
                        clave, valor = linea.split(':', 1)
                        representante[clave.strip()] = valor.strip()
                
                if 'ID' in representante:
                    self.id_representante = representante['ID']
                    self.entry_nombre_apellido.delete(0, tk.END)
                    self.entry_nombre_apellido.insert(0, representante.get('Nombre y Apellido', ''))
                    self.entry_cedula.delete(0, tk.END)
                    self.entry_cedula.insert(0, representante.get('Cédula', ''))
                    self.entry_telefono.delete(0, tk.END)
                    self.entry_telefono.insert(0, representante.get('Teléfono', ''))
                    self.entry_correo.delete(0, tk.END)
                    self.entry_correo.insert(0, representante.get('Correo', ''))
                    self.entry_direccion.delete(0, tk.END)
                    self.entry_direccion.insert(0, representante.get('Dirección', ''))
                    self.entry_serial_carnet.delete(0, tk.END)
                    self.entry_serial_carnet.insert(0, representante.get('Serial del Carnet', ''))
                    self.entry_codigo_carnet.delete(0, tk.END)
                    self.entry_codigo_carnet.insert(0, representante.get('Código del Carnet', ''))

            if self.id_representante is not None:
                
                # Llama a la función para eliminar el representante por ID
                eliminar_representante(self.id_representante)  # Reemplaza "eliminar" con la función real
                # Actualiza la lista de estudiantes
                self.lista_representantes = consultar_representante()  # Reemplaza "consultar" con la función real
                # Actualiza la tabla
                self.tabla_representantes()
                # Limpia la selección
                self.id_representante = None
                # Limpia la ventana de consulta
                limpiar_consulta()
            else:
                messagebox.showerror("Error", "Debes seleccionar un representante para eliminarlo.")
    
        # Crear una ventana emergente para ingresar los datos de búsqueda
        ventana_consultar = tk.Toplevel(self)
        ventana_consultar.title("Consultar Representante")
        ventana_consultar.iconbitmap("./img/lupa.ico")

        label_consultar_por = tk.Label(ventana_consultar, text="Consultar por:")
        label_consultar_por.grid(row=0, column=0)

        option_consultar_por = tk.StringVar()
        option_consultar_por.set("cedula")
        opciones_consultar_por = ["id_representante", "nombre_apellido", "cedula"]
        for i, opcion in enumerate(opciones_consultar_por):
            tk.Radiobutton(ventana_consultar, text=opcion, variable=option_consultar_por, value=opcion).grid(row=0, column=i+1)

        label_valor = tk.Label(ventana_consultar, text="Valor:")
        label_valor.grid(row=1, column=0)

        entry_valor = tk.Entry(ventana_consultar)
        entry_valor.grid(row=1, column=1)

        boton_consultar = tk.Button(ventana_consultar, text="Consultar", command=lambda: consultar_por_campo(option_consultar_por.get(), entry_valor.get()))
        boton_consultar.config(
            width=18, font=("Arial", 9, "bold"), fg="#DAD5D6",
            bg="#1658A2", cursor="hand2", activebackground="#3586DF")
        boton_consultar.grid(row=2, column=0, columnspan=2)

        # "Limpiar Consulta" que eliminará el valor ingresado en el campo de búsqueda 
        # y limpiará el área de texto que muestra los resultados de la consulta.
        boton_limpiar = tk.Button(ventana_consultar, text="Limpiar Consulta", command=lambda: limpiar_consulta())
        boton_limpiar.config(
            width=18, font=("Arial", 9, "bold"), fg="#45474B",
            bg="#F9D689", cursor="hand2", activebackground="#F5E7B2")
        boton_limpiar.grid(row=2, column=2, columnspan=2)

        # Agregar un widget de texto para mostrar los resultados
        resultado_text = tk.Text(ventana_consultar, height=10, width=50)
        resultado_text.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

        # Agregar un botón para editar y eliminar
        boton_editar = tk.Button(ventana_consultar, text="Editar Seleccionado", command=editar_datos_consulta_representante)
        boton_editar.config(
            width=18, font=("Arial", 9, "bold"), fg="#DAD5D6",
            bg="#158645", cursor="hand2", activebackground="#35BD6F")
        boton_editar.grid(row=4, column=0, columnspan=2)

        boton_eliminar = tk.Button(ventana_consultar, text="Eliminar Seleccionado", command=eliminar_datos_consulta_representante)
        boton_eliminar.config(
            width=18, font=("Arial", 9, "bold"), fg="#DAD5D6",
            bg="#BD152E", cursor="hand2", activebackground="#E15370")
        boton_eliminar.grid(row=4, column=2, columnspan=2)
        

        ventana_consultar.mainloop()
    