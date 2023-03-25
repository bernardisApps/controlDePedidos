import tkinter as tk
import tkinter.simpledialog as sd

class EditarCliente(sd.Dialog):

    resultado = ""

    def __init__(self, parent, title, cliente):
        self.cliente = cliente
        sd.Dialog.__init__(self,parent,title)

    def body(self,parent):
        
        self.nombre_variable = tk.StringVar()
        self.nombre_variable.set(self.cliente[1])
        self.apellido_variable = tk.StringVar()
        self.apellido_variable.set(self.cliente[2])
        self.direccion_variable = tk.StringVar()
        self.direccion_variable.set(self.cliente[3])
        self.celular_variable = tk.IntVar()
        self.celular_variable.set(self.cliente[4])
        
        tk.Label(parent, text="Nombre:").grid(row=0)
        tk.Label(parent, text="Apellido:").grid(row=1)
        tk.Label(parent, text="Dirección:").grid(row=2)
        tk.Label(parent, text="Celular:").grid(row=3)

        self.nombre_entry = tk.Entry(parent,textvariable=self.nombre_variable)
        self.apellido_entry = tk.Entry(parent,textvariable=self.apellido_variable)
        self.direccion_entry = tk.Entry(parent,textvariable=self.direccion_variable)
        self.celular_entry = tk.Entry(parent,textvariable=self.celular_variable)

        self.nombre_entry.grid(row=0, column=1)
        self.apellido_entry.grid(row=1, column=1)
        self.direccion_entry.grid(row=2, column=1)
        self.celular_entry.grid(row=3, column=1)

        return self.nombre_entry # Devuelve el primer widget para darle el foco
    
    def apply(self):
        if not self.nombre_variable == "" and not self.apellido_variable == "" and not self.direccion_variable == "" and not self.celular_variable == "": 
            self.resultado = {
                'id' : self.cliente[0],
                'nombre': self.nombre_entry.get(),
                'apellido': self.apellido_entry.get(),
                'direccion': self.direccion_entry.get(),
                'celular': self.celular_entry.get()
            }
        else:
            super().cancel()
    
    def cancel(self, event=None):
        super().cancel()
