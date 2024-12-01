import os
from dotenv import load_dotenv
import pymysql

print("SI HA ENTRADO EN INIT DATABASE.py")

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
    connection = pymysql.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=int(DB_PORT),
        database=DB_NAME
    )
    # print(DB_USER)
    # print(DB_PASSWORD)
    # print(DB_HOST)
    # print(DB_PORT)
    # print(DB_NAME)
    return connection

def check_record_exists(table_name, value):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = f"SELECT EXISTS(SELECT 1 FROM {table_name} WHERE word = %s)"
        cursor.execute(query, (value,))
        exists = cursor.fetchone()[0]
        return exists
    except Exception as e:
        print(f"Error checking record: {e}")
        return False
    finally:
        connection.close()

def create_word(table_name,word):
    # print("ENTRÓ EN FUNCIÓN 1")
    connection = get_db_connection()
    cursor = connection.cursor()
    
    
    exist = check_record_exists(table_name,word)
    
    flag = False
    if exist != 0:
        return flag
    else: 
        cursor.execute(f"INSERT INTO {table_name} (word) VALUES (%s)", (word,))
        
        # Confirmar los cambios
        connection.commit()
        print(f"Registro '{word}' creado en {table_name}")

        # Cerrar la conexión
        cursor.close()
        connection.close()
        flag = True
        return flag
    
def get_all_words_fn(table_name):
    # print("ENTRÓ EN FUNCIÓN 2")
    connection = get_db_connection()
    cursor = connection.cursor()

    # Obtener las palabras de la tabla correspondiente
    cursor.execute(f"SELECT word FROM {table_name}")
    # words = cursor.fetchall()
    words = [word[0] for word in cursor.fetchall()]

    # Cerrar la conexión
    cursor.close()
    connection.close()

    return words

def get_a_word_fn(table_name):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Obtener una palabra de la tabla correspondiente
    cursor.execute(f"""SELECT word FROM {table_name}
                        ORDER BY RAND() LIMIT 1""")
    word = cursor.fetchone()
    if word:
        print(f"Palabra aleatoria: {word[0]}")
    else:
        print("No se encontró ninguna palabra.")

    # Cerrar la conexión
    cursor.close()
    connection.close()

    return word

def remove_word_fn (table_name,word):
    connection = get_db_connection()
    cursor = connection.cursor()
    
    exist = check_record_exists(table_name, word)
    
    flag = False
    if exist == 1:
        cursor.execute(f"""
                       DELETE FROM {table_name}
                       WHERE word = %s;
                       """, (word,))
        
        # Confirmar los cambios
        connection.commit()
        
        print(f"Registro '{word}' eliminado de {table_name}")
        
        # Cerrar la conexión
        cursor.close()
        connection.close()
        flag = True
        return flag
    else:
        return flag
         
def move_word(source_table: str, target_table: str, word: str):
    try: 
        connection = get_db_connection()
        cursor = connection.cursor()
        
        # Paso 1: Insertar el registro en la tabla de destino
        insert_query = f"""
            INSERT INTO {target_table} (word)
            VALUES (%s)
        """
        cursor.execute(insert_query, (word,))
        # Confirmar los cambios
        connection.commit()
        
        # Paso 2: Eliminar el registro de la tabla de origen
        delete_query = f"""
            DELETE FROM {source_table}
            WHERE word = %s;
        """
        cursor.execute(delete_query, (word,))

        # Confirmar los cambios
        connection.commit()

        print(f"Registro '{word}' movido de {source_table} a {target_table}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        connection.rollback()

    finally:
        # Cerrar la conexión
        cursor.close()
        connection.close()


# connection = get_db_connection()
# cursor = connection.cursor()

# w = get_words("word_new_table")
# print("word_new_table:",w)
# w = get_words("word_learned_table")
# print("word_learned_table:",w)

# flag = remove_word("word_learned_table","XXX")
# print(flag)


# w = get_a_word("word_new_table")
# print(w)
# w = get_a_word("word_learned_table")
# print(w)
# w = get_a_word("word_learned_table")
# print(w)

# cursor.execute('SHOW DATABASES')
# print(cursor.fetchall())
# cursor.execute('SHOW TABLES')
# # cursor.fetchall()
# print(cursor.fetchall())

# query = f"""
#             DELETE FROM word_new_table
#             WHERE word = 'hello2';
#         """
# cursor.execute(query)
# # Confirmar los cambios
# connection.commit()

# query = f"""
#             INSERT INTO word_new_table (word)
#             VALUES ('XXX')
#         """
# cursor.execute(query)

# # Confirmar los cambios
# connection.commit()


# move_word("XXX", "word_new_table", "word_learned_table" )
# print("holii")