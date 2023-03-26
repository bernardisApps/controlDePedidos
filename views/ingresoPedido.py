import tkinter as tk
import tkinter.simpledialog as sd
from tkinter import ttk,messagebox
from database.modelo import Clientes,Pedidos

class NuevoPedidoDialog(sd.Dialog):
    def body(self, master):
        tk.Label(master, text="Cliente:").grid(row=0)
        tk.Label(master, text="Pedido:").grid(row=1)
        tk.Label(master, text="Precio:").grid(row=2)

        self.listaClientes = Clientes().traerTodos()

        self.nombresClientes = []

        for cliente in self.listaClientes:
            self.nombresClientes.append(str(cliente[0])+"-"+str(cliente[1]))

        self.cliente_combobox = ttk.Combobox(master,values=self.nombresClientes,width=30)
        self.pedido_entry = tk.Entry(master,width=30)
        self.precio_entry = tk.Entry(master,width=30)

        self.cliente_combobox.grid(row=0, column=1,padx=5,pady=5)
        self.pedido_entry.grid(row=1, column=1,padx=5,pady=5)
        self.precio_entry.grid(row=2, column=1,padx=5,pady=5)

        return self.cliente_combobox # Devuelve el primer widget para darle el foco
    
    def apply(self):
        if not self.cliente_combobox.get() == "" and not self.pedido_entry.get() == "" and not self.precio_entry.get() == "": 
            self.resultado = {
                'cliente': self.cliente_combobox.get().split("-")[1],
                'pedido': self.pedido_entry.get(),
                'precio': self.precio_entry.get(),
                'id_cliente' : int(self.cliente_combobox.get().split("-")[0])
            }
            rows = Pedidos().guardar(self.resultado['cliente'],self.resultado['precio'],self.resultado['pedido'],self.resultado['id_cliente'])
            if rows > 0:
                messagebox.showinfo(title="Agregar Pedido", message="Se guardó el pedido en la base de datos")
        else:
            messagebox.showerror(title="Agregar Pedido", message="Debe completar todos los campos")
            super().cancel()
    
    def cancel(self, event=None):
        super().cancel()