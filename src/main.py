import tkinter as tk
from client.gui_app import Frame, barra_menu

def main():
    # creacion de ventana
    root = tk.Tk()
    root.title("Lista de Estudiantes")
    root.iconbitmap("img/lists_list_6082.ico")
    root.resizable(0,0)
    
    #colocando barra de menu
    barra_menu(root)

    # creando contenedor dentro de la ventana
    app = Frame(root=root)

    app.mainloop()

if __name__ == '__main__':
    main()