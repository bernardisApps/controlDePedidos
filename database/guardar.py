import pandas as pd
import tkinter as tk
from tkinter import filedialog

class Guardar():

    def __init__(self,treeview) -> None:
        self.treeview = treeview
        self.save_to_excel(treeview)
    
    def treeviewToDataFrame(self,treeview):
        columns = []
        for column in treeview["columns"]:
            columns.append(column)

        rows = []
        for item in treeview.get_children():
            values = []
            for column in columns:
                values.append(treeview.item(item, "values")[columns.index(column)])
            rows.append(dict(zip(columns, values)))

        return pd.DataFrame(rows, columns=columns)
    
    
    def save_to_excel(self,treeview):
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".xlsx")
        if file_path:
            try:
                df = self.treeviewToDataFrame(treeview)
                df.to_excel(file_path, index=False)
                tk.messagebox.showinfo("Excel Guardado", f"El archivo de Excel se ha guardado en {file_path}")
            except:
                tk.messagebox.showerror("Error al Guardar", "Se ha producido un error al guardar el archivo de Excel.")

    
