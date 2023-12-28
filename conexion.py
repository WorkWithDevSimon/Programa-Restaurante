import cx_Oracle  # Importa  cx_Oracle para trabajar con bases de datos Oracle desde Python

class Conexion:
    def __init__(self):
        USER = "INACAP"  # Usuario para la conexión a la base de datos
        PASSWORD = "Oohackerx"  # Contraseña para la conexión a la base de datos
        DSN = "localhost/orcl"  # Ubicación de la base de datos Oracle
        self.conn = cx_Oracle.connect(user=USER, password=PASSWORD, dsn=DSN)  # Establece la conexión a la base de datos Oracle


