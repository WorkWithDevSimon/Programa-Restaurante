from conexion import Conexion


class Bebidas:
    def __init__(self):
        # self siempre va a hacer el metodo que llame al objeto
        self.id = None
        self.nombre = None
        self.precio = None
        self.tamaño = None
        self.disponibilidad = None

    def CargarBebidas(self):
        c = Conexion()
        datos_De_Bebias = []
        cursor = c.conn.cursor()
        resultado = cursor.execute(
            """select bebidas.id, bebidas.nombre,bebidas.precio,bebidas.tamaño,disponibilidad.nombre
          from bebidas INNER JOIN disponibilidad on bebidas.disponibilidad = disponibilidad.id """
        )
        for fila in resultado.fetchall():
            datos = (
                fila[0],  # ID
                fila[1],  # NOMBRE
                fila[2],  # PRECIO
                fila[3],  # TAMAÑO
                fila[4],  # DISPONIBILIDAD
            )
            datos_De_Bebias.append(datos)
           
        return datos_De_Bebias
        # esta funcion permite traer los datos de la base y agregarlos en su respectivas tablas
    
    def HabilitarBebida(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para actualizar la disponibilidad de una bebida en la tabla "bebidas"
        sql = "UPDATE bebidas SET disponibilidad = :A  WHERE id = :ID"
        # Ejecutar la consulta SQL con los parámetros ID y A (valor "1" para habilitar la bebida)
        resultado = cursor.execute(sql, ID=self.id, A="1")
        # Confirmar los cambios en la base de datos
        c.conn.commit()
        # Cerrar la conexión a la base de datos
        c.conn.close()

    def DeshabilitarBebida(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para actualizar la disponibilidad de una bebida en la tabla "bebidas"
        sql = "UPDATE bebidas SET disponibilidad = :A  WHERE id = :ID"
        # Ejecutar la consulta SQL con los parámetros ID y A (valor "2" para deshabilitar la bebida)
        resultado = cursor.execute(sql, ID=self.id, A="2")
        # Confirmar los cambios en la base de datos
        c.conn.commit()
        # Cerrar la conexión a la base de datos
        c.conn.close()

    def BebidaTotal(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para obtener información completa de una bebida en la tabla "bebidas" usando el parámetro ID
        sql = "SELECT id, nombre, precio, disponibilidad FROM bebidas WHERE id = :id"
        # Parámetros de la consulta SQL
        params = {'id': self.id}
        # Ejecutar la consulta SQL con los parámetros proporcionados
        cursor.execute(sql, params)
        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()
        # Actualizar los valores de nombre, precio y disponibilidad en el objeto Bebida si se encontró un resultado
        if resultado != None:
            self.nombre = resultado[1]
            self.precio = resultado[2]
            self.disponibilidad = resultado[3]
        # Devolver el resultado de la consulta
        return resultado

        