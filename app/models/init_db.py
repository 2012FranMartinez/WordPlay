import pymysql
from dotenv import load_dotenv
import os

# print("SI HA ENTRADO EN INIT DB")

# Cargar las variables de entorno
load_dotenv()
# Obtener las variables de entorno
DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PORT = os.getenv("MYSQL_PORT")
DB_NAME = os.getenv("MYSQL_DATABASE")

def create_tables():
    # Establecer la conexión
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    print(DB_USER)
    print(DB_PASSWORD)
    print(DB_HOST)
    print(DB_PORT)
    print(DB_NAME)
    # Crear un cursor para ejecutar las consultas
    cursor = connection.cursor()

    # Crear la base de datos si no existe
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

    # Seleccionar la base de datos creada
    cursor.execute(f"USE {DB_NAME}")

    # Consultas para crear las tablas
    create_word_new_table = """
    CREATE TABLE IF NOT EXISTS word_new_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        word VARCHAR(255) UNIQUE NOT NULL
    );
    """

    create_word_learned_table = """
    CREATE TABLE IF NOT EXISTS word_learned_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        word VARCHAR(255) UNIQUE NOT NULL
    );
    """

    # Ejecutar las consultas para crear las tablas
    cursor.execute(create_word_new_table)
    cursor.execute(create_word_learned_table)

    # Confirmar los cambios
    connection.commit()

    # Cerrar la conexión
    cursor.close()
    connection.close()

