from conexion import Conexion  # Importa la clase Conexion desde el módulo conexion

class Postres:
    def __init__(self):
        self.id = None  # ID del postre (inicializado como None)
        self.nombre = None  # Nombre del postre (inicializado como None)
        self.precio = None  # Precio del postre (inicializado como None)
        self.tamaño = None  # Tamaño del postre (inicializado como None)
        self.ingredientes = None  # Ingredientes del postre (inicializado como None)
        self.disponibilidad = None  # Disponibilidad del postre (inicializado como None)

    def CargarPostres(self):
        c = Conexion()
        datos_De_Postres = []
        cursor = c.conn.cursor()
        resultado = cursor.execute(
            """select postres.id,postres.nombre, postres.precio, postres.tamaño, postres.ingredientes,
          disponibilidad.nombre from postres inner join disponibilidad on postres.disponibilidad = disponibilidad.id """
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
            datos_De_Postres.append(datos)
            
        return datos_De_Postres

    def HabilitarPostre(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para actualizar la disponibilidad de un postre en la tabla "postres"
        sql = "UPDATE postres SET disponibilidad = :A  WHERE id = :ID"
        # Ejecutar la consulta SQL con los parámetros ID y A (valor "1" para habilitar el postre)
        resultado = cursor.execute(sql, ID=self.id, A="1")
        # Confirmar los cambios en la base de datos
        c.conn.commit()
        # Cerrar la conexión a la base de datos
        c.conn.close()

    def DeshabilitarPostre(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para actualizar la disponibilidad de un postre en la tabla "postres"
        sql = "UPDATE postres SET disponibilidad = :A  WHERE id = :ID"
        # Ejecutar la consulta SQL con los parámetros ID y A (valor "2" para deshabilitar el postre)
        resultado = cursor.execute(sql, ID=self.id, A="2")
        # Confirmar los cambios en la base de datos
        c.conn.commit()
        # Cerrar la conexión a la base de datos
        c.conn.close()

    def PostresTotal(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para obtener información completa de un postre en la tabla "postres"
        sql = "SELECT id, nombre, precio, disponibilidad FROM postres WHERE id = :id"
        # Parámetros de la consulta SQL
        params = {'id': self.id}
        # Ejecutar la consulta SQL con los parámetros
        cursor.execute(sql, params)
        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()
        # Actualizar los valores de nombre, precio y disponibilidad en el objeto Postre si se encontró un resultado
        if resultado != None:
            self.nombre = resultado[1]
            self.precio = resultado[2]
            self.disponibilidad = resultado[3]
        # Devolver el resultado de la consulta
        return resultado
