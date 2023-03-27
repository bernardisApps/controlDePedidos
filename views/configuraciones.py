import tkinter as tk
import tkinter.simpledialog as sd
from database.modelo import Configuraciones
from tkinter import messagebox

class EditarConfiguraciones(sd.Dialog):

    def body(self,parent):

        self.empresa_variable = tk.StringVar()
        self.empleado_variable = tk.StringVar()

        objeto = Configuraciones().recuperarObjeto()

        if objeto:
            self.empresa_variable.set(objeto['empresa'])
            self.empleado_variable.set(objeto['empleado'])
        else:
            print("no hay objeto")

        tk.Label(parent,text="Nombre Empresa: ").grid(row=0,column=0, padx=5,pady=5)

        self.empresa_entry = tk.Entry(parent,textvariable=self.empresa_variable)
        self.empresa_entry.grid(row=0,column=1, padx=5,pady=5)

        tk.Label(parent,text="Nombre Empleado: ").grid(row=1,column=0, padx=5,pady=5)

        self.empleado_entry = tk.Entry(parent,textvariable=self.empleado_variable)
        self.empleado_entry.grid(row=1,column=1, padx=5,pady=5)
    
    def apply(self):
        if not self.empresa_variable.get() == "" and not self.empleado_variable.get() == "":
            obj = {
                'empresa' : self.empresa_variable.get(),
                'empleado' : self.empleado_variable.get()
            }
            if Configuraciones().guardarObjeto(obj):
                messagebox.showinfo(title="Guardar configuraciones",message="Se han guardado las configuraciones")
            else:
                messagebox.showerror(title="Guardar configuraciones",message="No se han podido guardar las configuraciones")
        super().cancel()
    
    def cancel(self, event=None):
        super().cancel()