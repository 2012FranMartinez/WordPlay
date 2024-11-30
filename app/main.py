from fastapi import FastAPI
# from app.models import create_word, get_words
from app.models.models import create_word, get_words  # Importación de funciones desde models.py


app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Welcome to WordPlay API ;)"}

@app.post("/add_word/")
def add_word(word: str, table: str):
    """
    Inserta una nueva palabra en la tabla especificada.
    :param word: La palabra a insertar.
    :param table: La tabla en la que insertar la palabra (debe ser 'w_n' o 'w_y').
    """
    create_word(word, table)
    return {"message": f"Word '{word}' added to table '{table}'"}

@app.get("/get_words/{table}")
def get_all_words(table: str):
    """
    Obtiene todas las palabras de la tabla especificada.
    :param table: El nombre de la tabla ('w_n' o 'w_y').
    """
    words = get_words(table)
    return {"words": words}
