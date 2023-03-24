import tkinter as tk
from tkinter import ttk
from database.modelo import Pedidos
from tkinter import messagebox

class FramePrincipal(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()

    def buscar(self):
        if not self.nombre_variable.get() == "":
            pedidos = Pedidos().buscar(self.nombre_variable.get())
            if pedidos.__len__() > 0:
                self.treeview1.delete(*self.treeview1.get_children())
                for pedido in pedidos:
                    self.treeview1.insert("","end",text=pedido[0],values=(pedido[1],pedido[2],pedido[3]))
        else:
            messagebox.showinfo(title="Error", message="Debe llenar el campo de nombre")

    def eliminar(self):
        pass

    def createWidgets(self):

        self.nombre_variable = tk.StringVar()
        self.apellido_variable = tk.StringVar()
        self.direccion_variable = tk.StringVar()
        self.celular_variable = tk.IntVar()

        self.frame1 = tk.Frame(self.master,bg="lightgrey",width=180,relief="groove", bd=1)
        self.frame1.pack(expand=True,fill="y",side="left",anchor="w",padx=10,pady=10)

        tk.Label(self.frame1, text="Nombre: ").pack(padx=5,pady=5,anchor="w")

        self.nombre_entry = tk.Entry(self.frame1,textvariable=self.nombre_variable)
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

        self.boton_buscar = tk.Button(self.frame1,text="Buscar",command=self.buscar)
        self.boton_buscar.pack(padx=5,pady=5, fill="x")

        self.boton_eliminar = tk.Button(self.frame1,text="Eliminar",command=self.eliminar)
        self.boton_eliminar.pack(padx=5,pady=5, fill="x")

        ############Frame2#############

        self.frame2 = tk.Frame(self.master,bg="lightgrey",relief="groove", bd=1,width=600)
        self.frame2.pack(fill="both", padx=[0,10], pady=10, expand=True)

        self.treeview1 = ttk.Treeview(self.frame2,columns=("cliente","precio","pedido"))
        self.treeview1.heading("#0",text="ID")
        self.treeview1.heading("cliente",text="Cliente")
        self.treeview1.heading("precio",text="Precio")
        self.treeview1.heading("pedido",text="Pedido")
        self.treeview1.column("#0",width=30)
        self.treeview1.pack(padx=5,pady=5)

        #traer los datos desde la base de datos

        pedidos = Pedidos().obtenerTodos()

        for pedido in pedidos:
            self.treeview1.insert("","end",text=pedido[0],values=(pedido[1],pedido[2],pedido[3]))

