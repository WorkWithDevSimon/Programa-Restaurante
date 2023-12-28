from conexion import Conexion  # Importa la clase Conexion desde el módulo conexion

class Pedidos:
    def __init__(self):
        self.id = None  # ID del pedido (inicializado como None)
        self.comidas = None  # Comidas del pedido (inicializado como None)
        self.bebidas = None  # Bebidas del pedido (inicializado como None)
        self.postres = None  # Postres del pedido (inicializado como None)
        self.cantidad_de_comida = None  # Cantidad de comida del pedido (inicializado como None)
        self.cantidad_de_bebidas = None  # Cantidad de bebidas del pedido (inicializado como None)
        self.cantidad_de_postres = None  # Cantidad de postres del pedido (inicializado como None)
        self.total = None  # Total del pedido (inicializado como None)
        self.fechas = None  # Fechas del pedido (inicializado como None)
        self.Estados = None  # Estados del pedido (inicializado como None)

    def CargarPedido(self):
        c = Conexion()
        datos_De_Pedido = []
        cursor = c.conn.cursor()
        resultado = cursor.execute("SELECT * FROM pedido")
        for fila in resultado.fetchall():
            datos = (
                fila[0],  # ID
                fila[1],  # COMIDAS
                fila[2],  # BEBIDAS
                fila[3],  # POSTRES
                fila[4],  # CANTIDAD DE COMIDA
                fila[5],  # CANTIDAD DE BEBIDAS
                fila[6],  # CANTIDAD DE POSTRES
                fila[7],  # TOTAL
                fila[8],  # FECHA
                fila[9],  # ESTADO

            )
            datos_De_Pedido.append(datos)
            
                
        return datos_De_Pedido
    
    def AceptarPedido(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para actualizar el estado de un pedido a "Aceptado" en la tabla "pedido"
        sql = "UPDATE pedido SET estado = :A  WHERE id = :ID"
        # Ejecutar la consulta SQL con los parámetros ID y A (valor "Aceptado")
        resultado = cursor.execute(sql, ID=self.id, A="Aceptado")
        # Confirmar los cambios en la base de datos
        c.conn.commit()

    def RechazarPedido(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para actualizar el estado de un pedido a "Rechazado" en la tabla "pedido"
        sql = "UPDATE pedido SET estado = :R  WHERE id = :ID"
        # Ejecutar la consulta SQL con los parámetros ID y R (valor "Rechazado")
        resultado = cursor.execute(sql, ID=self.id, R="Rechazado")
        # Confirmar los cambios en la base de datos
        c.conn.commit()

    def EliminarPedido(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para eliminar un pedido de la tabla "pedido" usando el parámetro ID
        sql = "DELETE FROM pedido WHERE ID = :id"
        # Ejecutar la consulta SQL con el parámetro ID
        cursor.execute(sql, id=self.id)
        # Confirmar los cambios en la base de datos
        c.conn.commit()
        c.conn.close()

    
    def CrearPedido(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para insertar un nuevo pedido en la tabla "pedido" con los valores proporcionados
        sql = """INSERT INTO pedido (comidas, bebidas, postres, cantidad_comidas, cantidad_bebidas, cantidad_postres, total, fecha, estado)
                VALUES (:comidas, :bebidas, :postres, :cantidad_comidas, :cantidad_bebidas, :cantidad_postres, :total, CURRENT_TIMESTAMP, 'Pendiente')"""
        # Ejecutar la consulta SQL con los parámetros proporcionados
        resultado = cursor.execute(sql, comidas=self.comidas, bebidas=self.bebidas, postres=self.postres,
                                cantidad_comidas=self.cantidad_de_comida, cantidad_bebidas=self.cantidad_de_bebidas,
                                cantidad_postres=self.cantidad_de_postres, total=self.total)
        # Confirmar los cambios en la base de datos
        c.conn.commit()
        c.conn.close()

        
    def EditarPedido(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para actualizar los datos de un pedido en la tabla "pedido" usando el parámetro ID
        sql = """UPDATE pedido SET comidas = :co, bebidas = :be, postres = :po, cantidad_comidas = :cco,
                cantidad_bebidas = :cbe, cantidad_postres = :cpo, total = :total, fecha = CURRENT_TIMESTAMP,
                estado = 'Pendiente' WHERE ID = :id"""
        # Ejecutar la consulta SQL con los parámetros proporcionados
        cursor.execute(sql, co=self.comidas, be=self.bebidas,
                      po=self.postres, cco=self.cantidad_de_comida,
                      cbe=self.cantidad_de_bebidas, cpo=self.cantidad_de_postres,
                      total=self.total, id=self.id)
    
        # Confirmar los cambios en la base de datos
        c.conn.commit()
        c.conn.close()
    def CapEstado(self):
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para obtener el estado de un pedido específico en la tabla "pedido" usando el parámetro ID
        sql = "SELECT estado FROM pedido WHERE id = :id"
        # Ejecutar la consulta SQL con el parámetro ID
        cursor.execute(sql, id=self.id)
        resultado = cursor.fetchone()
        if resultado is not None:
            self.Estados = resultado[0]
        return resultado