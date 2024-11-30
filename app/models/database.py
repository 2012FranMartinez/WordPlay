import os
from dotenv import load_dotenv
import pymysql

# db = pymysql.connect(host = os.getenv('MYSQL_HOST'),
#                      user = os.getenv('MYSQL_USER'),
#                      password = os.getenv('MYSQL_PASSWORD'),
#                      cursorclass = pymysql.cursors.DictCursor
# )
# cursor = db.cursor()

load_dotenv(dotenv_path="../.env")

DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_HOST = os.getenv("MYSQL_HOST")
DB_PORT = os.getenv("MYSQL_PORT")
DB_NAME = os.getenv("MYSQL_DATABASE")

def get_db_connection():
    """
    Establece una conexión con la base de datos MySQL usando las credenciales del archivo .env
    """
    connection = pymysql.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=int(DB_PORT),
        database=DB_NAME
    )
    return connection



