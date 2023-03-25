import tkinter as tk
from tkinter import ttk
from database.modelo import Pedidos,Clientes
from tkinter import messagebox

class FramePrincipal(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()

    def buscar(self,*args):
        if not self.nombre_variable.get() == "":
            pedidos = Pedidos().buscar(self.nombre_variable.get())
            if pedidos.__len__() > 0:
                self.treeview1.delete(*self.treeview1.get_children())
                for pedido in pedidos:
                    self.treeview1.insert("","end",text=pedido[0],values=(pedido[1],pedido[2],pedido[3]))
        else:
            self.refrescarTreeview()

    def eliminar(self):
        seleccion = self.treeview1.focus()
        id = self.treeview1.item(seleccion)['text']
        if not id=="":
            row = Pedidos().eliminarID(id)
            if row > 0 :
                messagebox.showinfo(title="Eliminando Pedido", message="Se ha eliminado el pedido de la base de datos")
                self.refrescarTreeview()

    def treeviewSeleccion(self,*args):
        seleccion = self.treeview1.focus()
        if seleccion:
            nombre = self.treeview1.item(seleccion)['values'][0]
            cliente = Clientes().buscar(nombre)
            self.nombre_variable.set(cliente[1])
            self.apellido_variable.set(cliente[2])
            self.direccion_variable.set(cliente[3])
            self.celular_variable.set(cliente[4])
            
    def refrescarTreeview(self):
        #traer los datos desde la base de datos
        for i in self.treeview1.get_children():
            self.treeview1.delete(i)

        pedidos = Pedidos().obtenerTodos()

        for pedido in pedidos:
            self.treeview1.insert("","end",text=pedido[0],values=(pedido[1],pedido[2],pedido[3]))

    def limpiarEntrys(self,*args):
        self.nombre_variable.set("")
        self.apellido_variable.set("")
        self.direccion_variable.set("")
        self.celular_variable.set("")

    def createWidgets(self):

        self.nombre_variable = tk.StringVar()
        self.apellido_variable = tk.StringVar()
        self.direccion_variable = tk.StringVar()
        self.celular_variable = tk.IntVar()

        ###################Frame1#############################

        self.frame1 = tk.Frame(self.master,bg="lightgrey",width=180,relief="groove", bd=1)
        self.frame1.pack(side="left",anchor="w",padx=5,pady=5,fill="y")

        tk.Label(self.frame1, text="Nombre: ").pack(padx=5,pady=5,anchor="w")

        self.nombre_entry = tk.Entry(self.frame1,textvariable=self.nombre_variable)
        self.nombre_entry.bind("<Return>",self.buscar)
        self.nombre_entry.bind("<Button-1>",self.limpiarEntrys)
        self.nombre_entry.focus()
        self.nombre_entry.pack(padx=5,pady=5)

        tk.Label(self.frame1, text="Apellido: ").pack(padx=5,pady=5,anchor="w")

        self.apellido_entry = tk.Entry(self.frame1,textvariable=self.apellido_variable)
        self.apellido_entry.pack(padx=5,pady=5)

        tk.Label(self.frame1, text="Dirección: ").pack(padx=5,pady=5,anchor="w")

        self.direccion_entry = tk.Entry(self.frame1,textvariable=self.direccion_variable)
        self.direccion_entry.pack(padx=5,pady=5)

        tk.Label(self.frame1, text="Celular: ").pack(padx=5,pady=5,anchor="w")

        self.celular_entry = tk.Entry(self.frame1,textvariable=self.celular_variable)
        self.celular_entry.pack(padx=5,pady=5)

        self.boton_buscar = tk.Button(self.frame1,text="Buscar(enter)",command=self.buscar)
        self.boton_buscar.pack(padx=5,pady=5, fill="x")

        ############Frame2#############

        self.frame2 = tk.Frame(self.master,bg="lightgrey",relief="groove", bd=1)
        self.frame2.pack(expand=True,fill="both",side="left",anchor="w",padx=5,pady=5)

        self.treeview1 = ttk.Treeview(self.frame2,columns=("cliente","precio","pedido"))
        self.treeview1.heading("#0",text="ID")
        self.treeview1.heading("cliente",text="Cliente")
        self.treeview1.heading("precio",text="Precio")
        self.treeview1.heading("pedido",text="Pedido")
        self.treeview1.column("#0",width=30)
        self.treeview1.column("cliente",width=100)
        self.treeview1.column("precio",width=100)
        self.treeview1.column("pedido",width=200)
        self.treeview1.pack(padx=5,pady=5,fill="x")
        self.refrescarTreeview()

        #boton para seleccionar elemento

        self.btn_treeviewSelect = tk.Button(self.frame2,text="seleccionar",command=self.treeviewSeleccion)
        self.btn_treeviewSelect.pack(padx=5,pady=5,side="right",anchor="n")

        #boton eliminar
        self.boton_eliminar = tk.Button(self.frame2,text="Eliminar",command=self.eliminar)
        self.boton_eliminar.pack(padx=5,pady=5,side="right",anchor="n")

