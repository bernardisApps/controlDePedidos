import tkinter as tk
import tkinter.simpledialog as sd
from database.modelo import Clientes
from tkinter import messagebox

class NuevoClienteDialog(sd.Dialog):
    
    def body(self, master):
        tk.Label(master, text="Nombre:").grid(row=0)
        tk.Label(master, text="Apellido:").grid(row=1)
        tk.Label(master, text="Dirección:").grid(row=2)
        tk.Label(master, text="Celular:").grid(row=3)

        self.nombre_entry = tk.Entry(master)
        self.apellido_entry = tk.Entry(master)
        self.direccion_entry = tk.Entry(master)
        self.celular_entry = tk.Entry(master)

        self.nombre_entry.grid(row=0, column=1)
        self.apellido_entry.grid(row=1, column=1)
        self.direccion_entry.grid(row=2, column=1)
        self.celular_entry.grid(row=3, column=1)

        return self.nombre_entry # Devuelve el primer widget para darle el foco
    
    def apply(self):
        if not self.nombre_entry.get() == "" and not self.apellido_entry.get() == "" and not self.direccion_entry.get() == "" and not self.celular_entry.get() == "": 
            if self.celular_entry.get().__len__() < 10 or self.nombre_entry.get().__len__() < 2 or self.apellido_entry.get().__len__() < 5:
                messagebox.showerror(title="Nuevo Cliente", message="Los datos ingresados no son correctos")
                super().cancel()
            else:
                self.resultado = {
                    'nombre': self.nombre_entry.get(),
                    'apellido': self.apellido_entry.get(),
                    'direccion': self.direccion_entry.get(),
                    'celular': self.celular_entry.get()
                }
                rows = Clientes().nuevo(self.resultado['nombre'],self.resultado['apellido'],self.resultado['direccion'],self.resultado['celular'])
                if rows > 0:
                    messagebox.showinfo(title="Nuevo Cliente",message="Se agregó el nuevo cliente a la base de datos")
        else:
            messagebox.showerror(title="Nuevo Cliente", message="Debe completar todos los campos")
            super().cancel()
    
    def cancel(self, event=None):
        super().cancel()