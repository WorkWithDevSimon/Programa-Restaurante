from conexion import Conexion  # Importa la clase Conexion desde el módulo conexion

class Comida:
    def __init__(self):
        self.id = None  # ID de la comida (inicializado como None)
        self.nombre = None  # Nombre de la comida (inicializado como None)
        self.precio = None  # Precio de la comida (inicializado como None)
        self.tamaño = None  # Tamaño de la comida (inicializado como None)
        self.ingredientes = None  # Ingredientes de la comida (inicializado como None)
        self.disponibilidad = None  # Disponibilidad de la comida (inicializado como None)

    def CargarComida(self):
        c = Conexion()
        datos_De_Comida = []
        cursor = c.conn.cursor()
        resultado = cursor.execute(
            """select comida.id,comida.nombre,comida.precio,comida.tamaño, comida.ingredientes,disponibilidad.nombre 
            from comida INNER JOIN disponibilidad on comida.disponibilidad = disponibilidad.id"""
        )
        for fila in resultado.fetchall():
            datos = (
                fila[0],  # ID
                fila[1],  # NOMBRE
                fila[2],  # PRECIO
                fila[3],  # TAMAÑO
                fila[4],  # INGREDIENTES
                fila[5],  # DISPONIBILIDAD
            )

            datos_De_Comida.append(datos)

        return datos_De_Comida

    def HabilitarComida(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para actualizar la disponibilidad de una comida en la tabla "comida"
        sql = "UPDATE comida SET disponibilidad = :A  WHERE id = :ID"
        # Ejecutar la consulta SQL con los parámetros ID y A (valor "1" para habilitar la comida)
        resultado = cursor.execute(sql, ID=self.id, A="1")
        # Confirmar los cambios en la base de datos
        c.conn.commit()
        # Cerrar la conexión a la base de datos
        c.conn.close()

    def DeshabilitarComida(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para actualizar la disponibilidad de una comida en la tabla "comida"
        sql = "UPDATE comida SET disponibilidad = :A  WHERE id = :ID"
        # Ejecutar la consulta SQL con los parámetros ID y A (valor "2" para deshabilitar la comida)
        resultado = cursor.execute(sql, ID=self.id, A="2")
        # Confirmar los cambios en la base de datos
        c.conn.commit()
        # Cerrar la conexión a la base de datos
        c.conn.close()

    def ComidaTotal(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para obtener información completa de una comida en la tabla "comida"
        sql = "SELECT id, nombre, precio, disponibilidad FROM comida WHERE id = :id"
        # Parámetros de la consulta SQL
        params = {'id': self.id}
        # Ejecutar la consulta SQL con los parámetros
        cursor.execute(sql, params)
        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()
        # Actualizar los valores de nombre, precio y disponibilidad en el objeto Comida si se encontró un resultado
        if resultado != None:
            self.nombre = resultado[1]
            self.precio = resultado[2]
            self.disponibilidad = resultado[3]
        # Devolver el resultado de la consulta
        return resultado

            

