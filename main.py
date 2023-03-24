import tkinter as tk
from views.framePrincipal import FramePrincipal

root = tk.Tk()
root.title("Gestión de pedidos")
root.geometry("800x480")
root.resizable(False,False)
menu_principal = tk.Menu(root,tearoff=0)
root.config(menu=menu_principal)
framePrincipal = FramePrincipal(master=root)

def guardar():
    print("Guardando archivo...")

def salir():
    root.destroy()

def editar_cliente():
    print("Editando cliente...")

def editar_pedido():
    print("Editando pedido...")

def acerca_de():
    print("Acerca de esta aplicación...")

# Opción Archivo
menu_archivo = tk.Menu(menu_principal,tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Guardar", command=guardar)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

# Opción Editar
menu_editar = tk.Menu(menu_principal,tearoff=0)
menu_principal.add_cascade(label="Editar", menu=menu_editar)
menu_editar.add_command(label="Editar Cliente", command=editar_cliente)
menu_editar.add_command(label="Editar Pedido", command=editar_pedido)

# Opción Ayuda
menu_ayuda = tk.Menu(menu_principal,tearoff=0)
menu_principal.add_cascade(label="Ayuda",menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de...", command=acerca_de)


root.mainloop()