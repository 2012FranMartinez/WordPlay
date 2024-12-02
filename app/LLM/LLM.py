# from transformers import pipeline

# # Inicia sesión con tu API key
# from huggingface_hub import login
# login('tu-api-key-aqui')

# # Crear un pipeline de conversación con DialoGPT
# chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# # Iniciar una conversación
# response = chatbot("¡Hola, ¿cómo estás?")
# print(response)


# import requests
import os

# # URL de la API de Hugging Face para el modelo
# # model_name = "microsoft/DialoGPT-medium"
# # model_name = "facebook/blenderbot-400M-distill"
# model_name = "DeepPavlov/bert-base-spanish-wwm-uncased"
# api_url = f"https://api-inference.huggingface.co/models/{model_name}"

# # Tu API key
# HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
# headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

# # Texto de entrada
# input_text = {"inputs": "¡Hola, ¿cómo estás?"}

# # Realizar la solicitud POST
# response = requests.post(api_url, headers=headers, json=input_text)

# # Imprimir la respuesta
# print(response.json())

# -----------------------
# import time
# import requests
# from langchain.schema import HumanMessage

# model_name = "meta-llama/Llama-3.2-1B"
# model_name = "microsoft/DialoGPT-medium"
# api_url = f"https://api-inference.huggingface.co/models/{model_name}"

# HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# headers = {
#     "Authorization": f"Bearer {HUGGINGFACE_API_KEY}"
# }

# input_text = {
#     "inputs": "Eres un experto chef, ¿qué receta fácil me recomiendas para la cena?"
# }

# # response = requests.post(api_url, headers=headers, json=input_text)

# while True:
#     response = requests.post(api_url, headers=headers, json=input_text)
#     result = response.json()

#     if "error" in result and "loading" in result["error"]:
#         print(f"El modelo se está cargando. Tiempo estimado: {result.get('estimated_time', 'Desconocido')} segundos.")
#         time.sleep(5)  # Espera antes de volver a intentar
#     else:
#         break

# print(response.json())
# -----------------------

import os
import requests
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate,PromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEndpoint

# # # Configurar el modelo de Hugging Face
# # def load_llm(prompt: str):
# #     # model_name = "meta-llama/Llama-3.2-1B"
# #     # model_name = "microsoft/DialoGPT-medium"
# #     model_name = "Qwen/Qwen2.5-72B-Instruct"
    
# #     # Configura el modelo desde Hugging Face
# #     llm = ChatOpenAI(
# #         endpoint_url=f"https://api-inference.huggingface.co/models/{model_name}",
# #         huggingfacehub_api_token=os.getenv('API_KEY_MODEL'),
# #         temperature=0.3,
# #         max_length=2000
# #     )
    
# #     # Plantilla para el modelo
# #     prompt_template = ChatPromptTemplate.from_messages([
# #         ("system", prompt),
# #         MessagesPlaceholder(variable_name="history"),
# #         ("human", "{input}")
# #     ])
    
# #     runnable = prompt_template | llm
    
# #     # Historial de sesiones
# #     store = {}
# #     def get_session_history(session_id: str) -> BaseChatMessageHistory:
# #         if session_id not in store:
# #             store[session_id] = ChatMessageHistory()
# #         return store[session_id]
    
# #     with_message_history = RunnableWithMessageHistory(
# #         runnable,
# #         get_session_history,
# #         input_messages_key="input",
# #         history_messages_key="history"
# #     )
    
# #     return with_message_history

# # # Guardar en la base de datos (AWS API)
# # def save_to_database_local(word: str):
# #     api_url = "http://127.0.0.1:8000/add_word/"  # Endpoint local de tu API
# #     data = {
# #         "table_name": "word_new_table",  # Nombre de la tabla donde guardarás la palabra
# #         "word": word               # Palabra que se va a guardar
# #     }
# #     headers = {"Content-Type": "application/json"}
    
# #     try:
# #         response = requests.post(api_url, json=data, headers=headers)
# #         response.raise_for_status()  # Lanza una excepción si el status_code no es 2xx
# #         print(response.json()["message"])  # Muestra el mensaje del servidor
# #     except requests.exceptions.RequestException as e:
# #         print(f"Error al guardar en la base de datos: {e}")

# # # Función principal
# # def translate_and_store(word: str, session_id: str):
# #     # Prompt para el LLM
# #     prompt = """
# #     Eres un modelo experto en idiomas. Quiero que traduzcas palabras del inglés al español.
# #     Además, proporciona una frase de ejemplo en inglés utilizando las palabras dadas.
# #     """
    
# #     # Cargar el LLM
# #     llm = load_llm(prompt)
    
# #     # Generar la traducción y la frase
# #     input_text = f"Por favor, traduce esta palabra: '{word}' y dame una frase de ejemplo en inglés usándola."
# #     result = llm.invoke({"input": input_text, "session_id": session_id})
    
# #     # Guardar en la base de datos
# #     save_to_database_local(word)
    
# #     # Imprimir resultado
# #     print("Traducción y ejemplo generados:")
# #     print(result)
# #     return result

# # # Ejecución
# # if __name__ == "__main__":
# #     session_id = "user1_session"  # Esto podría ser dinámico según el usuario
# #     word_to_translate = "happiness"  # Ejemplo de palabra a traducir
# #     output = translate_and_store(word_to_translate, session_id)
# #     print(output)


# def load_llm(prompt):
#     # llm = HuggingFaceEndpoint(endpoint_url='https://api-inference.huggingface.co/models/Qwen/Qwen2.5-72B-Instruct',
#     llm = HuggingFaceEndpoint(endpoint_url='https://api-inference.huggingface.co/models/microsoft/Phi-3.5-mini-instruct',
#                           huggingfacehub_api_token=os.getenv('HUGGINGFACE_API_KEY'),
#                           temperature=0.3, max_lenght=500)
#     prompt_template = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             prompt,
#          ),
#          MessagesPlaceholder(variable_name='history'),
#          ('human', '{input}')
#     ]
#     )
#     runnable = prompt_template | llm
#     store = {}
    
#     def get_session_history(session_id: str) -> BaseChatMessageHistory:
#         if session_id not in store:
#             store[session_id] = ChatMessageHistory()
#         return store[session_id]
#     with_message_history = RunnableWithMessageHistory(
#     runnable,
#     get_session_history,
#     input_messages_key="input",
#     history_messages_key="history"
#     )
#     return with_message_history



# x = load_llm("Eres un experto en inglés. Que es goalkeeper")

# print(x)
# x.invoke({"input":"Traduceme valor a ingles y hazme unafrase con goalkeeper"}, config={'configurable': {'session_id': '1'}})
# print("holi")



# import time

# def load_llm(prompt):
#     llm = HuggingFaceEndpoint(
#         endpoint_url='https://api-inference.huggingface.co/models/microsoft/Phi-3.5-mini-instruct',
#         huggingfacehub_api_token=os.getenv('HUGGINGFACE_API_KEY'),
#         temperature=0.3, 
#         max_length=500
#     )
#     prompt_template = ChatPromptTemplate.from_messages(
#         [("system", prompt),
#          MessagesPlaceholder(variable_name='history'),
#          ('human', '{input}')]
#     )
#     runnable = prompt_template | llm
#     store = {}

#     def get_session_history(session_id: str) -> BaseChatMessageHistory:
#         if session_id not in store:
#             store[session_id] = ChatMessageHistory()
#         return store[session_id]
    
#     with_message_history = RunnableWithMessageHistory(
#         runnable,
#         get_session_history,
#         input_messages_key="input",
#         history_messages_key="history"
#     )
#     return with_message_history

# x = load_llm("Eres un experto en inglés. Qué es un goalkeeper?")
# print("-------------------------")
# print(x)

# # Añadir un pequeño retraso
# time.sleep(10)  # Esperar 10 segundos antes de la siguiente solicitud

# x.invoke({"input": "Traduceme valor a inglés y hazme una frase con goalkeeper"}, config={'configurable': {'session_id': '1'}})
# print("-------------------------")


from langchain.prompts import ChatPromptTemplate
from langchain.llms import HuggingFaceEndpoint

def load_llm(prompt):
    # Asegúrate de que el endpoint es correcto y que el modelo está cargado
    llm = HuggingFaceEndpoint(
        endpoint_url='https://api-inference.huggingface.co/models/microsoft/Phi-3.5-mini-instruct',
        huggingfacehub_api_token=os.getenv('HUGGINGFACE_API_KEY'),
        temperature=0.3,
        max_length=500
    )

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", prompt),
            ("human", '{input}')
        ]
    )

    # Ejecutar solo el modelo con el prompt
    response = llm.invoke({"input": "Tradúceme 'goalkeeper' al español"})
    print(response)
    return response

# Probar el modelo con un ejemplo
load_llm("Eres un experto en inglés. Qué significa goalkeeper?")
print("-----------")
