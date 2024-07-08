import tkinter as tk
from tkinter import ttk
from client.gui_app import Frame_estudiantes
from client.gui_app2 import Frame_representantes
from model.estudiantes_dao import crear_tabla, borrar_tabla
from model.representantes import crear_tabla_representantes, borrar_tabla_representantes

def main():
    # creacion de ventana
    root = tk.Tk()
    root.title("Lista de Estudiantes y Representantes")
    root.iconbitmap("img/lists_list_6082.ico")
    root.resizable(0,0)

    # create un notebook
    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True)

    # creando frames
    estudiantes = Frame_estudiantes(root)
    representantes = Frame_representantes(root)

    # creado barras de menú para cada frame

    def borrar_y_actualizar_tabla_estudiantes(estudiantes):
        borrar_tabla()
        estudiantes.actualizar_tabla_estudiantes()
    
    def borrar_y_actualizar_tabla_representantes(representantes):
        borrar_tabla_representantes()
        representantes.actualizar_tabla_representantes()

    # Barra menú estudiantes
    menu_estudiantes = tk.Menu(root)
    root.config(menu=menu_estudiantes, width=300, height=300)
    # menu de inicio
    menu_inicio = tk.Menu(menu_estudiantes, tearoff=0)
    menu_estudiantes.add_cascade(label="Inicio", menu=menu_inicio)
    # opciones dentro del menu de inicio
    menu_inicio.add_command(label="Crear Base de Datos Estudiantes", command=crear_tabla)
    menu_inicio.add_command(label="Eliminar Base de Datos Estudiantes", command=lambda: borrar_y_actualizar_tabla_estudiantes(estudiantes))
    menu_inicio.add_command(label="Salir", command=root.destroy)
    
    # Barra menú representantes
    menu_representantes = tk.Menu(root)
    root.config(menu=menu_representantes, width=300, height=300)
    # menu de inicio
    menu_inicio = tk.Menu(menu_representantes, tearoff=0)
    menu_representantes.add_cascade(label="Inicio", menu=menu_inicio)
    menu_inicio.add_command(label="Crear Base de Datos Representantes", command=crear_tabla_representantes)
    menu_inicio.add_command(label="Eliminar Base de Datos Representantes", command=lambda: borrar_y_actualizar_tabla_representantes(representantes))
    menu_inicio.add_command(label="Salir", command=root.destroy)
    
    estudiantes.pack(fill='both', expand=True)
    representantes.pack(fill='both', expand=True)

    # add frames to notebook
    notebook.add(estudiantes, text='Estudiantes')
    notebook.add(representantes, text='Representantes')

    # Evento para cambiar de menú según que ventana este abierta
    def on_tab_changed(_event):
        match notebook.tab(notebook.select(), "text"):
            case "Estudiantes":
                root.configure(menu=menu_estudiantes)
            case "Representantes":
                root.configure(menu=menu_representantes)

    notebook.bind('<<NotebookTabChanged>>', on_tab_changed)

    root.mainloop()

if __name__ == '__main__':
    main()
    