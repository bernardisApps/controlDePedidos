import sqlite3

class Pedidos:

    def __init__(self):
        self.conexion = sqlite3.connect("database/pedidos.db")
        self.cursor = self.conexion.cursor()

    def guardar(self,cliente,precio,pedido):
        if not cliente == "" and not precio == "" and not pedido == "":
            self.cliente = cliente
            self.precio = precio
            self.pedido = pedido
            sql = f"insert into pedidos (cliente , precio, pedido) values ('{self.cliente}', {self.precio}, '{self.pedido}')"
            self.cursor.execute(sql)
            self.conexion.commit()
            rowcounts = self.cursor.rowcount
            self.conexion.close()
            return rowcounts
            
        
    def obtenerTodos(self):
        sql = f"select * from pedidos"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        self.conexion.close()
        return rows
    
    def buscar(self,cliente):
        '''
        if not cliente == "":
            sql = f"select * from pedidos where cliente = '{cliente}'"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return rows'''
        # Crear una consulta SQL para buscar las filas que contienen la cadena de búsqueda
        consulta = "SELECT * FROM pedidos WHERE cliente LIKE ?"

        # Ejecutar la consulta y obtener los resultados
        self.cursor.execute(consulta, ('%' + cliente + '%',))
        resultados = self.cursor.fetchall()
        return resultados
    
    def eliminarID(self,id):
        sql = f"delete from pedidos where id = {id}"
        self.cursor.execute(sql)
        self.conexion.commit()
        rowafected = self.cursor.rowcount
        self.conexion.close()
        return rowafected
        
class Clientes:

    def __init__(self):
        self.conexion = sqlite3.connect("database/pedidos.db")
        self.cursor = self.conexion.cursor()

    def nuevo(self, nombre, apellido, direccion, celular):
        if not nombre == "" and not apellido == "" and not direccion == "" and not celular == 0:
            sql = f"insert into clientes (nombre, apellido, direccion, celular) values ('{nombre}', '{apellido}', '{direccion}', {celular})" 
            self.cursor.execute(sql)
            self.conexion.commit()
            rowcounts = self.cursor.rowcount
            self.conexion.close()
            return rowcounts
    
    def buscar(self,nombre):
        if not nombre == "":
            sql = f"select * from clientes where nombre = '{nombre}'"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            self.conexion.close()
            return rows
        
    def buscarID(self,id):
        if not id == "":
            sql = f"select * from clientes where nombre = '{id}'"
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            self.conexion.close()
            return row
        
    def eliminarID(self,id):
        sql = f"delete from clientes where id = {id}"
        self.cursor.execute(sql)
        self.conexion.commit()
        rowafected = self.cursor.rowcount
        self.conexion.close()
        return rowafected
        

