# import os
# import sys
# sys.path.append("../app")
# print(os.getcwd())

from fastapi import FastAPI,HTTPException
from app.models.database import create_word, get_words  
from pydantic import BaseModel

from fastapi import FastAPI
from .models.init_db import create_tables  # Importar la función para crear tablas

app = FastAPI()

# @app.on_event("startup")
# async def startup():
#     # Llamar a la función para crear las tablas al iniciar la aplicación
#     create_tables()

class New_record(BaseModel):
    word: str
    table_name:str
class Get_table(BaseModel):
    table_name:str

@app.get("/")
async def home():
    return {"message": "Welcome to WordPlay API ;)"}

@app.post("/add_word/")
async def add_word(new_record:New_record):
    try:
        create_word(new_record.table_name, new_record.word)
        return dict({"message": f"Word '{new_record.word}' added to table '{new_record.table_name}'"})
    except Exception as e:
        # Lanza una excepción HTTP con el mensaje del error capturado
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")

@app.get("/get_all_words/{table}")
async def get_all_words(get_table: Get_table):
    try:
        words = get_all_words(get_table.table_name)
        return dict({"words": words})
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")

@app.get("/get_a_word/{table}")
async def get_a_word(get_table:Get_table):
    try:
        word = get_a_word(get_table.table_name)
        return dict({"word": word})
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")

@app.delete("/remove_word/{table}")
async def remove_word(get_table:Get_table):
    try:
        flag = remove_word(get_table.table_name)
        return dict({"flag": flag})
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")




# @app.get("/get_words/{table}")
# def get_all_words(table: str):
#     words = get_words(table)
#     return {"words": words}
