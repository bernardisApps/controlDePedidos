import tkinter as tk
import tkinter.simpledialog as sd

class EditarPedido(sd.Dialog):

    resultado = ""

    def __init__(self, parent, title, pedido):
        self.pedido = pedido
        sd.Dialog.__init__(self,parent,title)

    def body(self,parent):
        
        self.cliente_variable = tk.StringVar()
        self.cliente_variable.set(self.pedido[1])
        self.precio_variable = tk.IntVar()
        self.precio_variable.set(self.pedido[2])
        self.pedido_variable = tk.StringVar()
        self.pedido_variable.set(self.pedido[3])
        
        tk.Label(parent, text="Cliente:").grid(row=0)
        tk.Label(parent, text="Precio:").grid(row=1)
        tk.Label(parent, text="Pedido:").grid(row=2)

        self.cliente_entry = tk.Entry(parent,textvariable=self.cliente_variable)
        self.precio_entry = tk.Entry(parent,textvariable=self.precio_variable)
        self.pedido_entry = tk.Entry(parent,textvariable=self.pedido_variable)

        self.cliente_entry.grid(row=0, column=1)
        self.precio_entry.grid(row=1, column=1)
        self.pedido_entry.grid(row=2, column=1)

        return self.cliente_entry # Devuelve el primer widget para darle el foco
    
    def apply(self):
        if not self.cliente_variable == "" and not self.precio_variable == "" and not self.pedido_variable == "": 
            self.resultado = {
                'id' : self.pedido[0],
                'cliente': self.cliente_entry.get(),
                'precio': self.precio_entry.get(),
                'pedido': self.pedido_entry.get()
            }
        else:
            super().cancel()
    
    def cancel(self, event=None):
        super().cancel()