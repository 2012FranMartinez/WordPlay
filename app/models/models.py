# app/models/models.py
from .database import get_db_connection

def create_word(word, table_name):
    """
    Inserta una nueva palabra en la tabla especificada.
    :param word: La palabra que quieres insertar.
    :param table_name: El nombre de la tabla donde se insertará la palabra ('w_n' o 'w_y').
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    # Insertar la palabra en la tabla correspondiente
    cursor.execute(f"INSERT INTO {table_name} (word) VALUES (%s)", (word,))
    
    # Confirmar los cambios
    connection.commit()

    # Cerrar la conexión
    cursor.close()
    connection.close()

def get_words(table_name):
    """
    Obtiene todas las palabras de la tabla especificada.
    :param table_name: El nombre de la tabla de la que obtener las palabras ('w_n' o 'w_y').
    :return: Lista de palabras en la tabla.
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    # Obtener las palabras de la tabla correspondiente
    cursor.execute(f"SELECT word FROM {table_name}")
    words = cursor.fetchall()

    # Cerrar la conexión
    cursor.close()
    connection.close()

    return words
