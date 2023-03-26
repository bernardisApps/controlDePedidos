import tkinter as tk
import tkinter.simpledialog as sd
from tkinter import messagebox
from database.modelo import Clientes

class EditarCliente(sd.Dialog):

    def __init__(self, parent,title,id):
        self.id = id
        super().__init__(parent, title)

    def body(self,parent):
        
        self.cliente = Clientes().buscarID(self.id)
        
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
                "nombre" : self.nombre_variable.get(),
                "apellido" : self.apellido_variable.get(),
                "direccion" : self.direccion_variable.get(),
                "celular" : self.celular_variable.get()
            }
            rows = Clientes().actualizarCliente(self.id,self.nombre_variable.get(),self.apellido_variable.get(),self.direccion_variable.get(),self.celular_variable.get())
            if rows > 0:
                messagebox.showinfo(title="Editar Cliente", message=f"Cliente de id:{self.id} se ha editado correctamente")
                return self.resultado
        else:
            messagebox.showerror(title="Editar Cliente", message="Debe completar todos los campos")
            super().cancel()
    
    def cancel(self, event=None):
        super().cancel()
