# Usar una imagen base de Python
FROM python:3.12-bullseye
# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app
# Copiar el archivo de requisitos para instalar las dependencias
COPY ./ejercicio/requirements.txt /app/requirements.txt
# Instalar las dependencias desde el archivo requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
# Copiar los archivos del proyecto a la raíz del contenedor
COPY ./app_model.py /app/app_model.py
COPY ./ejercicio /app/ejercicio
# Exponer el puerto que usará FastAPI (5000 en tu caso)
EXPOSE 5000
# Comando para iniciar la aplicación con Uvicorn
CMD ["uvicorn", "app_model:app", "--host", "0.0.0.0", "--port", "5000"]