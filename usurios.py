from conexion import Conexion  # Importa la clase Conexion desde el módulo conexion

class Usuario:
    def __init__(self):
        self.id = None  # ID del usuario (inicializado como None)
        self.usuario = None  # Nombre de usuario (inicializado como None)
        self.contraseña = None  # Contraseña del usuario (inicializado como None)
        self.tipo_usu_id = None  # ID del tipo de usuario (inicializado como None)


    def login(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para buscar un usuario por nombre de usuario y contraseña
        sql = "SELECT * FROM usuarios WHERE usuario = :u AND contraseña = :p"
        params = {'u': self.usuario, 'p': self.contraseña}
        cursor.execute(sql, params)
        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()
        # Verificar si se encontró un resultado
        if resultado is not None:
            # Actualizar el valor de tipo_usu_id en el objeto Usuario
            self.tipo_usu_id = resultado[3]
        # Devolver el resultado de la consulta (puede ser None si no se encontró el usuario)
        return resultado

    def CargarUsuarios(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        # Crear una lista para almacenar los datos de los usuarios
        datos_De_Usuario = []
        cursor = c.conn.cursor()
        # Consulta SQL para obtener los datos de los usuarios junto con su tipo de usuario
        resultado = cursor.execute(
            """SELECT usuarios.id, usuarios.usuario, tipo_usu.tipo_usuario 
            FROM usuarios
            INNER JOIN tipo_usu ON tipo_usu.id = usuarios.tipo_usu_id"""
        )
        # Recorrer los resultados de la consulta
        for fila in resultado.fetchall():
            # Extraer los datos de cada fila
            datos = (
                fila[0],  # ID
                fila[1],  # NOMBRE
                fila[2],  # TIPO DE USUARIO
            )
            # Agregar los datos a la lista
            datos_De_Usuario.append(datos)
        # Devolver la lista de datos de usuarios
        return datos_De_Usuario

    
    def EliminarUsuario(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para eliminar un usuario por ID
        sql = "DELETE FROM usuarios WHERE ID = :id"
        # Ejecutar la consulta SQL con el parámetro ID
        cursor.execute(sql, id=self.id)
        # Confirmar los cambios en la base de datos
        c.conn.commit()
        # Cerrar la conexión a la base de datos
        c.conn.close()
        
    def ContarAdmin(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para contar el número de usuarios con tipo_usu_id igual a 1 (admin)
        sql = "SELECT COUNT(*) FROM usuarios WHERE tipo_usu_id = 1"
        # Ejecutar la consulta SQL
        cursor.execute(sql)
        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()[0]
        # Devolver el resultado de la consulta
        return resultado

    def CapTipoUsuario(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para obtener el tipo_usu_id de un usuario por su ID
        sql = "SELECT tipo_usu_id FROM usuarios WHERE id = :id"
        # Ejecutar la consulta SQL con el parámetro ID
        cursor.execute(sql, id=self.id)
        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()
        # Devolver el tipo_usu_id si se encontró un resultado, de lo contrario devolver None
        return resultado[0] if resultado else None

    def CrearUsuario(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para insertar un nuevo usuario en la tabla "usuarios"
        sql = "INSERT INTO usuarios (usuario, contraseña, tipo_usu_id) VALUES (:usuario, :contraseña, :tipo_usu)"
        # Ejecutar la consulta SQL con los parámetros de usuario, contraseña y tipo_usu_id
        cursor.execute(sql, usuario=self.usuario, contraseña=self.contraseña, tipo_usu=self.tipo_usu_id)
        # Confirmar los cambios en la base de datos
        c.conn.commit()
        # Cerrar la conexión a la base de datos
        c.conn.close()

    def EditarUsuario(self):
        # Establecer conexión a la base de datos
        c = Conexion()
        cursor = c.conn.cursor()
        # Consulta SQL para actualizar los datos de un usuario en la tabla "usuarios"
        sql = """UPDATE usuarios SET usuario = :usuario, contraseña = :contraseña, tipo_usu_id = :tipo_usu  WHERE id = :id """
        # Ejecutar la consulta SQL con los parámetros de usuario, contraseña, tipo_usu_id e id
        cursor.execute(sql, usuario=self.usuario, contraseña=self.contraseña, tipo_usu=self.tipo_usu_id, id=self.id)
        # Confirmar los cambios en la base de datos
        c.conn.commit()
        # Cerrar la conexión a la base de datos
        c.conn.close()


 
 