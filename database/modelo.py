import sqlite3
import pickle

class Pedidos:

    def __init__(self):
        self.conexion = sqlite3.connect("database/pedidos.db")
        self.cursor = self.conexion.cursor()

    def guardar(self,cliente,precio,pedido,id_cliente):
        if not cliente == "" and not precio == "" and not pedido == "" and not id_cliente == "":
            self.cliente = cliente
            self.precio = precio
            self.pedido = pedido
            self.id_cliente = id_cliente
            sql = f"insert into pedidos (cliente , precio, pedido, id_cliente) values ('{self.cliente}', {self.precio}, '{self.pedido}',{self.id_cliente})"
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
    
    def buscarID(self,id):
        # Crear una consulta SQL para buscar las filas que contienen la cadena de búsqueda
        consulta = f"SELECT * FROM pedidos WHERE id = {id}"

        # Ejecutar la consulta y obtener los resultados
        self.cursor.execute(consulta)
        resultados = self.cursor.fetchone()
        return resultados
    
    def actualizarPedido(self,id,cliente,pedido,precio):
        sql = f"update pedidos set cliente='{cliente}', pedido='{pedido}', precio = {precio} where id = {id}"
        self.cursor.execute(sql)
        self.conexion.commit()
        rowafected = self.cursor.rowcount
        self.conexion.close()
        return rowafected
        
class Clientes:

    def __init__(self):
        self.conexion = sqlite3.connect("database/pedidos.db")
        self.cursor = self.conexion.cursor()

    def traerTodos(self):
        sql = f"select * from clientes"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        self.conexion.close()
        return rows

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
            rows = self.cursor.fetchone()
            self.conexion.close()
            return rows
        
    def traerNombres(self):
        sql = f"select * from clientes"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        self.conexion.close()
        resultado = []
        for row in rows:
            resultado.append(row[1])
        return resultado
    
    def traerNombresApellidos(self):
        sql = f"select * from clientes"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        self.conexion.close()
        resultado = []
        for row in rows:
            resultado.append(row[1]+" "+row[2])
        return resultado
        
    def buscarID(self,id):
        if not id == "":
            sql = f"select * from clientes where id = '{id}'"
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
    
    def eliminarNombreApellido(self,nombre,apellido):
        sql = f"delete from clientes where nombre='{nombre}' and apellido = '{apellido}'"
        self.cursor.execute(sql)
        self.conexion.commit()
        rowafected = self.cursor.rowcount
        self.conexion.close()
        return rowafected
    
    def actualizarCliente(self,id,nombre,apellido,direccion,celular):
        sql = f"update clientes set nombre='{nombre}', apellido='{apellido}', direccion = '{direccion}', celular = {celular} where id = {id}"
        self.cursor.execute(sql)
        self.conexion.commit()
        rowafected = self.cursor.rowcount
        self.conexion.close()
        return rowafected

class Configuraciones():

    def guardarObjeto(self,objeto):
        try:
            with open('configuraciones.bin', 'wb') as archivo:
                pickle.dump(objeto, archivo)
            return True
        except:
            return False

    def recuperarObjeto(self):
        try:
            with open('configuraciones.bin', 'rb') as archivo:
                objeto_recuperado = pickle.load(archivo)
                return objeto_recuperado
        except:
            return None
        

