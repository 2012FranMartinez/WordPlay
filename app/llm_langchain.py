from huggingface_hub import InferenceClient
from langchain import PromptTemplate
import os



# Definir el contenido del prompt
template_j = """Analiza esta frase "{sentence}" como si fueras un profesor muy exigente de lingüística inglesa. Contesta en los siguientes puntos:
1/ Si está correcta sintácticamente EN INGLÉS y qué mejorarías para la próxima vez.
2/ Si tiene sentido lo que he escrito a nivel de vocabulario y sintaxis EN INGLÉS.
3/ Si la frase tiene sentido a nivel de vocabulario y sintaxis EN INGLÉS, devuelve unicamente la palabra: True; si no la palabra: False"""

# Definir el contenido del prompt
template_t = """Traduceme esta palabra o frase de inglés a español: {sentence}. Y además ponme una frase de ejemplo"""


def get_prompt_template(option): 
    if option == "j": 
        return PromptTemplate(input_variables=["sentence"], template=template_j) 
    elif option == "t": 
        return PromptTemplate(input_variables=["sentence"], template=template_t)


# # Crear el prompt template
# prompt = PromptTemplate(input_variables=["sentence"], template=template)

# Función para formatear el prompt
# def format_prompt(sentence):
#     return prompt.format(sentence=sentence)

def format_prompt(sentence, prompt_template): 
    return prompt_template.format(sentence=sentence)

# Función para obtener la respuesta del modelo
def get_model_response(api_key, model, formatted_prompt):
    client = InferenceClient(api_key=api_key)
    
    messages = [
        {
            "role": "user",
            "content": formatted_prompt
        }
    ]
    
    completion = client.chat.completions.create(
        model=model, 
        messages=messages, 
        max_tokens=350
    )
    
    return completion.choices[0].message.content

