from fastapi import FastAPI,HTTPException
# from app.models.database import create_word, get_words  
from app.models.database import * 
from pydantic import BaseModel

import logging
# Configuración básica de logging
logging.basicConfig(level=logging.DEBUG)

from fastapi import FastAPI
from .models.init_db import create_tables  # Importar la función para crear tablas

app = FastAPI()

# @app.on_event("startup")
# async def startup():
#     # Llamar a la función para crear las tablas al iniciar la aplicación
#     create_tables()

class Word(BaseModel):
    table_name:str
    word: str
class Get_table(BaseModel):
    table_name:str

@app.get("/")
async def home():
    return {"message": "Welcome to WordPlay API ;)"}

@app.post("/add_word/")
async def add_word(word:Word):
    try:
        logging.debug(f"param tabla: {word.table_name} y param word{word.word}")
        flag = create_word(word.table_name, word.word)
        logging.debug(f"Word '{word.word}' added to table '{word.table_name}'")
        return dict({"message": f"Word '{word.word}' added to table '{word.table_name}'",
                     "flag":flag})
    except Exception as e:
        # Lanza una excepción HTTP con el mensaje del error capturado
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")

@app.delete("/remove_word/")
async def remove_word(word:Word):
    try:
        logging.debug(f"tabla: {word.table_name}")
        logging.debug(f"word: {word.table_name}")
        flag = remove_word_fn(word.table_name,word.word)
        logging.debug(f"flag: {flag}")
        
        if flag: 
            return dict({"message": f"Word '{word.word}' removed from table '{word.table_name}'",
                        "flag":flag})
        else:
            return dict({"message": f"Word '{word.word}' dosn´t removed from table '{word.table_name} bacause dosn´t exist'",
                        "flag":flag})
            
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")

@app.get("/get_all_words/")
async def get_all_words(get_table: Get_table):
    try:
        logging.debug(f"Recibiendo la solicitud para la tabla: {get_table.table_name}")
        words = get_all_words_fn(get_table.table_name)
        logging.debug(f"Palabras obtenidas: {words}")
        return dict({"words": words})
    except Exception as e:
        logging.error(f"Error al obtener las palabras: {str(e)}")
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")

@app.get("/get_a_word/")
async def get_a_word(get_table:Get_table):
    try:
        logging.debug(f"tabla: {get_table.table_name}")
        word = get_a_word_fn(get_table.table_name)
        logging.debug(f"palabra retornada: {word}")
        return dict({"word": word})
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")
