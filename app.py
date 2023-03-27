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
from views.acercade import AcercaDe
import os
from views.configuraciones import EditarConfiguraciones

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Gestión de Pedidos")
        self.resizable(False,False)
        self.geometry("800x480")
        self.menu_principal = tk.Menu(self,tearoff=0)
        self.config(menu=self.menu_principal)
        self.bind("<Control-n>",self.nuevoCliente)
        self.bind("<Control-p>",self.nuevoPedido)
        self.bind("<Control-s>",self.guardar)
        self.archivoDeConfiguracion()
        self.createWidgets()

    def archivoDeConfiguracion(self):
        nombreArchivo = "configuraciones.bin"
        if os.path.exists(nombreArchivo):
            print(f"El archivo '{nombreArchivo}' ya existe.")
        else:
            # Crear el archivo
            with open(nombreArchivo, "wb") as archivo:
                print(f"Se ha creado el archivo '{nombreArchivo}'.")

    def createWidgets(self):
        self.framePrincipal = FramePrincipal(self)
        #Opción Archivo
        menu_archivo = tk.Menu(self.menu_principal,tearoff=0)
        self.menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Nuevo Cliente", command=self.nuevoCliente)
        menu_archivo.add_command(label="Nuevo Pedido", command=self.nuevoPedido)
        menu_archivo.add_command(label="Guardar", command=self.guardar)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.salir)

        # Opción Editar
        menu_editar = tk.Menu(self.menu_principal,tearoff=0)
        self.menu_principal.add_cascade(label="Editar", menu=menu_editar)
        menu_editar.add_command(label="Editar Cliente", command=self.editar_cliente)
        menu_editar.add_command(label="Editar Pedido", command=self.editar_pedido)
        menu_editar.add_command(label="Eliminar Cliente", command=self.eliminarCliente)

        # Opción Ayuda
        menu_ayuda = tk.Menu(self.menu_principal,tearoff=0)
        self.menu_principal.add_cascade(label="Ayuda",menu=menu_ayuda)
        menu_ayuda.add_command(label="Acerca de...", command=self.acerca_de)

        # Opción empresa
        menu_empresa = tk.Menu(self.menu_principal,tearoff=0)
        self.menu_principal.add_cascade(label="Empresa",menu=menu_empresa)
        menu_empresa.add_command(label="Configuraciones",command=self.editar_configuraciones)

    def guardar(self,*args):
        Guardar(self.framePrincipal.treeview1)

    def salir(self):
        self.destroy()

    def editar_cliente(self):
        if not self.framePrincipal.idClienteSeleccion == None:
            dlg = EditarCliente(self,title="Editar Cliente",id=self.framePrincipal.idClienteSeleccion)
            if dlg.resultado:
                self.framePrincipal.actualizarVariables(dlg.resultado)
        else:
            messagebox.showinfo(title="Error", message="Debe seleccionar primero un cliente")

    def editar_pedido(self):
        if not self.framePrincipal.idPedidoSeleccion == None:
            dlg = EditarPedido(self, title="Editar Pedido",pedido=Pedidos().buscarID(self.framePrincipal.idPedidoSeleccion))
            if dlg.resultado:
                guardado =  Pedidos().actualizarPedido(dlg.resultado['id'],dlg.resultado['cliente'],dlg.resultado['pedido'],dlg.resultado['precio'])
                if guardado > 0:
                    messagebox.showinfo(title="Editar Pedido", message="Se ha actualizado el pedido")
                    self.framePrincipal.refrescarTreeview()
        else:
            messagebox.showerror(title="Error", message="Debe seleccionar un pedido")
                
    def acerca_de(self):
        AcercaDe(self,title="Acerca de")

    def nuevoCliente(self,*args):
        dlg = NuevoClienteDialog(self, title="Nuevo Cliente")

    def nuevoPedido(self,*args):
        dlg = NuevoPedidoDialog(self, title="Nuevo Pedido")
        self.framePrincipal.refrescarTreeview()

    def eliminarCliente(self):
        EliminarCliente(self,title="Eliminar Cliente")
    
    def editar_configuraciones(self):
        EditarConfiguraciones(self,title="Editar configuraciones")