import tkinter as tk
from views.framePrincipal import FramePrincipal
from views.ingresoCliente import NuevoClienteDialog
from views.ingresoPedido import NuevoPedidoDialog
from database.modelo import Clientes,Pedidos
from tkinter import messagebox

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
    print("Acerca de esta aplicación")

def nuevoCliente():
    dlg = NuevoClienteDialog(root, title="Nuevo Cliente")
    if not dlg.resultado == "":
        guardado = Clientes().nuevo(dlg.resultado["nombre"],dlg.resultado["apellido"],dlg.resultado["direccion"],dlg.resultado["celular"])
        if guardado > 0:
            messagebox.showinfo(title="Nuevo Cliente", message="Cliente agregado con éxito a la base de datos")

def nuevoPedido():
    dlg = NuevoPedidoDialog(root, title="Nuevo Pedido")
    if not dlg.resultado == "":
        guardado = Pedidos().guardar(dlg.resultado["cliente"],dlg.resultado["precio"],dlg.resultado["pedido"])
        if guardado > 0:
            messagebox.showinfo(title="Nuevo Pedido", message="El nuevo pedido ha sido guardado en la base de datos")
            framePrincipal.refrescarTreeview()

# Opción Archivo
menu_archivo = tk.Menu(menu_principal,tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Nuevo Cliente", command=nuevoCliente)
menu_archivo.add_command(label="Nuevo Pedido", command=nuevoPedido)
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