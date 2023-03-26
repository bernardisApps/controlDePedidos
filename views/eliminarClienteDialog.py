import tkinter as tk
import tkinter.simpledialog as sd
from tkinter import ttk,messagebox
from database.modelo import Clientes

class EliminarCliente(sd.Dialog):

    def body(self,parent):
        
        tk.Label(parent, text="Cliente:").grid(row=0)
        self.cliente_combobox = ttk.Combobox(parent,values=Clientes().traerNombresApellidos(),width=30)
        self.cliente_combobox.grid(row=0, column=1,padx=5,pady=5)
    
    def apply(self):
        array_nombre = self.cliente_combobox.get().split(" ")
        nombre = array_nombre[0]
        apellido = array_nombre[1]
        resultado = Clientes().eliminarNombreApellido(nombre,apellido)
        if resultado > 0:
            messagebox.showinfo(title="Eliminar cliente", message="Cliente Eliminado de la base de datos")
        super().cancel()
    
    def cancel(self, event=None):
        super().cancel()
