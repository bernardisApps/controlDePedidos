import tkinter as tk
from views.framePrincipal import FramePrincipal
from views.ingresoCliente import NuevoClienteDialog
from views.ingresoPedido import NuevoPedidoDialog
from views.editarClienteDialog import EditarCliente
from views.editarPedido import EditarPedido
from database.modelo import Clientes,Pedidos
from database.guardar import Guardar
from tkinter import messagebox
from views.eliminarClienteDialog import EliminarCliente

root = tk.Tk()
root.title("Gestión de pedidos")
root.geometry("800x480")
root.resizable(False,False)
menu_principal = tk.Menu(root,tearoff=0)
root.config(menu=menu_principal)
framePrincipal = FramePrincipal(master=root)

def guardar(*args):
    guardado = Guardar(framePrincipal.treeview1)

def salir():
    root.destroy()

def editar_cliente():
    if not framePrincipal.idClienteSeleccion == "":
        dlg = EditarCliente(root,title="Editar Cliente",id=framePrincipal.idClienteSeleccion)
        framePrincipal.actualizarVariables(dlg.resultado)
    else:
        messagebox.showinfo(title="Error", message="Debe seleccionar primero un cliente")

def editar_pedido():
    if not framePrincipal.idPedidoSeleccion == None:
        dlg = EditarPedido(root, title="Editar Pedido",pedido=Pedidos().buscarID(framePrincipal.idPedidoSeleccion))
        if not dlg.resultado == "":
            guardado =  Pedidos().actualizarPedido(dlg.resultado['id'],dlg.resultado['cliente'],dlg.resultado['pedido'],dlg.resultado['precio'])
            if guardado > 0:
                messagebox.showinfo(title="Editar Pedido", message="Se ha actualizado el pedido")
                framePrincipal.refrescarTreeview()
    else:
        messagebox.showerror(title="Error", message="Debe seleccionar un pedido")
            
def acerca_de():
    print("Acerca de esta aplicación")

def nuevoCliente(*args):
    dlg = NuevoClienteDialog(root, title="Nuevo Cliente")

def nuevoPedido(*args):
    dlg = NuevoPedidoDialog(root, title="Nuevo Pedido")
    framePrincipal.refrescarTreeview()

def eliminarCliente():
    EliminarCliente(root,title="Eliminar Cliente")

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
menu_editar.add_command(label="Eliminar Cliente", command=eliminarCliente)

# Opción Ayuda
menu_ayuda = tk.Menu(menu_principal,tearoff=0)
menu_principal.add_cascade(label="Ayuda",menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de...", command=acerca_de)


root.bind("<Control-n>",nuevoCliente)
root.bind("<Control-p>",nuevoPedido)
root.bind("<Control-s>",guardar)

root.mainloop()