import streamlit as st
import os
import sys
from main import *
import logging
import asyncio
import aiohttp
import requests

# sys.path.append('../')
from llm_langchain import *
from dotenv import load_dotenv  # Carga las variables de entorno desde el archivo .env 
logging.debug(f"si llega")

# Carga las variables de entorno
load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
# API_BASE_URL = os.getenv("API_BASE_URL")
api_key = os.getenv("HUGGINGFACE_API_KEY")
model = "microsoft/Phi-3.5-mini-instruct"
        
# Función para mostrar la página principal
def main_page():
    st.title("WordPlay: Aprende inglés jugando")

    # Campo de texto para ingresar la palabra o frase
    user_input = st.text_input("Escribe una frase usando la palabra...")

    # Botón para traducir
    if st.button("Traducir"):
        
        data = { "table_name": "word_new_table", "word": user_input }
        response = requests.post("http://127.0.0.1:8000/add_word/", json=data)
        
        prompt_template = get_prompt_template("t")
        
        # Formatear el prompt 
        formatted_prompt = format_prompt(user_input, prompt_template)
        response = get_model_response(api_key, model, formatted_prompt)

        st.write(response)

    # Espaciado
    st.write("")
    st.write("")

    # Botón Jugar grande y azul
    if st.button("Jugar", key="jugar"):
        st.session_state.page = "jugar"


def juego_page():

    # Datos para la solicitud
    data = {"table_name": "word_new_table"}

    # Hacer la solicitud a la API para obtener la palabra
    response = requests.get("http://127.0.0.1:8000/get_a_word/", json=data)
    
    print(response)

    if response.status_code == 200:
        palabra_acertar = response.json().get("word", "No se encontró ninguna palabra.")
    else:
        palabra_acertar = "No se encontró ninguna palabra."
        st.write(f"Error en la solicitud: {response.status_code} - {response.text}")

    st.title(f"PALABRA A APRENDER:{palabra_acertar}")
    
    if palabra_acertar:
        # Mostrar la palabra subrayada
        # st.markdown(f"<u>{palabra_acertar}</u>", unsafe_allow_html=True)

        # Cuadro de texto estilo chat
        user_input = st.text_input(f"Escribe una frase en inglés usando la palabra '{palabra_acertar}'")

        # Botón para comprobar (verde)
        if st.button("Comprobar"):
            st.write(f"Frase ingresada: {user_input}")
                       
            prompt_template = get_prompt_template("j")
            
            # Formatear el prompt 
            formatted_prompt = format_prompt(user_input, prompt_template)
            response = get_model_response(api_key, model, formatted_prompt)

            st.write(response)
            
            

            # # Generar el prompt y obtener respuesta del modelo
            # sentence = user_input
            # formatted_prompt = format_prompt(sentence, "{0}")
            # response = get_model_response("api_key", "model", formatted_prompt)
            # st.write(response)

        # Estilos adicionales para el botón
        st.markdown(
            """
            <style>
            .stButton > button {
                background-color: green;
                color: white;
                width: 100%;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.write("No se encontró ninguna palabra en la base de datos.")




# Función para mostrar la página del juego
# def juego_page():
#     st.title("PALABRA A APRENDER:")
    
#     # Construir la URL dinámica 
#     url = f"{API_BASE_URL}/get_a_word/"
    
#     data = {"table_name": "word_new_table"}
    
#     response = requests.get("http://127.0.0.1:8000/get_a_word/", params=data)
#     if response.status_code == 200:
#         palabra_acertar = response.json().get("word", "No se encontró ninguna palabra.")
#     else:
#         palabra_acertar = "No se encontró ninguna palabra."
#         st.write(f"Error en la solicitud: {response.status_code} - {response.text}")
        
        
        
    
#     if response.status_code == 200:
#         st.markdown(f"<u>{palabra_acertar}</u>", unsafe_allow_html=True)
#         user_input = st.text_input(f"Escribe una frase en inglés usando la palabra {palabra_acertar}")
        
        
    
#     print(response)
    
    # palabra_acertar = response['word']
    
    # if response.status_code == 200:
    #     palabra_acertar = response.json().get("word", "No se encontró ninguna palabra.")
    # else:
    #     palabra_acertar = "No se encontró ninguna palabra."
    
    
    
    
    
    
    
    
    
    
    
    
    # if palabra_acertar:
    #     st.markdown(f"<u>{palabra_acertar}</u>", unsafe_allow_html=True)
        
    #     user_input = st.text_input(f"Escribe una frase en inglés usando la palabra {palabra_acertar}")
        
    #     if st.button("Comprobar"):
    #         st.write(f"Frase ingresada: {user_input}")
    #         sentence = user_input
    #         formatted_prompt = format_prompt(sentence, "{0}")
    #         response = get_model_response("api_key", "model",)
    #         st.write(response)
            
        
        
        
        
    
    
    # data = { "table_name": "word_new_table" } 
    # palabra_acertar = get_a_word_fn(data["table_name"])
    
    # data = {"table_name": "word_new_table"}
    # palabra_acertar = get_a_word(data["table_name"])
    # st.success(palabra_acertar)
    
    # # Crear un bucle de eventos para gestionar la llamada asíncrona 
    # loop = asyncio.new_event_loop() 
    # asyncio.set_event_loop(loop) 
    # palabra_acertar = loop.run_until_complete(get_a_word(data))
    
    
    # # Palabra subrayada
    # st.markdown(f"<u>{palabra_acertar}</u>", unsafe_allow_html=True)

    # # Cuadro de texto estilo chat
    # user_input = st.text_input(f"Escribe una frase en inglés usando la palabra {palabra_acertar}")

    # # Botón para comprobar (verde)
    # if st.button("Comprobar"):
    #     st.write(f"Frase ingresada: {user_input}")
    #     sentence = user_input
    #     formatted_prompt = format_prompt(sentence, "{0}")
    #     response = get_model_response(api_key, model, formatted_prompt)
        
    #     st.write(response)
        
        
    # Estilos adicionales para el botón
    st.markdown("""
        <style>
        .stButton > button {
            background-color: green;
            color: white;
            width: 100%;
        }
        </style>
    """, unsafe_allow_html=True)

# Condición para cambiar de página
if "page" not in st.session_state:
    st.session_state.page = "main"

# Lógica de navegación
if st.session_state.page == "main":
    main_page()
elif st.session_state.page == "jugar":
    juego_page()

