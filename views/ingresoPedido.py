import tkinter as tk
import tkinter.simpledialog as sd
from tkinter import ttk
from database.modelo import Clientes

class NuevoPedidoDialog(sd.Dialog):
    resultado = ""
    def body(self, master):
        tk.Label(master, text="Cliente:").grid(row=0)
        tk.Label(master, text="Pedido:").grid(row=1)
        tk.Label(master, text="Precio:").grid(row=2)

        self.cliente_combobox = ttk.Combobox(master,values=Clientes().traerNombres(),width=30)
        self.pedido_entry = tk.Entry(master,width=30)
        self.precio_entry = tk.Entry(master,width=30)

        self.cliente_combobox.grid(row=0, column=1,padx=5,pady=5)
        self.pedido_entry.grid(row=1, column=1,padx=5,pady=5)
        self.precio_entry.grid(row=2, column=1,padx=5,pady=5)

        return self.cliente_combobox # Devuelve el primer widget para darle el foco
    
    def apply(self):
        if not self.cliente_combobox.get() == "" and not self.pedido_entry.get() == "" and not self.precio_entry.get() == "": 
            self.resultado = {
                'cliente': self.cliente_combobox.get(),
                'pedido': self.pedido_entry.get(),
                'precio': self.precio_entry.get()
            }
        else:
            super().cancel()
    
    def cancel(self, event=None):
        super().cancel()