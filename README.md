# WordPlay
¡Bienvenido a Aprende Inglés Jugando! 🎮 Una aplicación interactiva diseñada para mejorar tu vocabulario y habilidades gramaticales en inglés de manera divertida y práctica.
📜 Descripción
Esta aplicación te permite traducir palabras del inglés al castellano con la ayuda de un modelo de lenguaje (LLM). A medida que traduces palabras, estas se almacenan en una base de datos alojada en AWS. Más adelante, puedes jugar con estas palabras para consolidar tu aprendizaje:

Traducción: Busca palabras en inglés y obtén su traducción al castellano.
Juego:
Se selecciona aleatoriamente una de las palabras que has buscado.
Formulas una frase utilizando la palabra.
Un modelo de lenguaje (LLM) evalúa si tu frase es gramaticalmente correcta y si captaste el significado de la palabra.
Si aciertas, ¡recibes felicitaciones! 🎉
Si no, la aplicación te muestra:
La traducción correcta.
Una frase de ejemplo.
Te invita a intentarlo de nuevo.
🚀 Funcionalidades
Traducción de palabras: Consulta palabras en inglés y obtén su significado en castellano.
Almacenamiento de palabras: Guarda automáticamente las palabras que consultas en una base de datos segura en AWS.
Juego interactivo: Practica construyendo frases con las palabras aprendidas, recibiendo retroalimentación en tiempo real.
🛠️ Tecnologías Utilizadas
Frontend: Framework web interactivo (por ejemplo, Streamlit, Flask).
Backend:
Modelo de Lenguaje (LLM): Para traducción y evaluación de frases.
Base de Datos (AWS): DynamoDB o RDS para almacenar las palabras aprendidas.
Despliegue en la nube: Infraestructura basada en AWS para garantizar escalabilidad y disponibilidad.
💡 Cómo usar
Instalación:

Clona el repositorio:
git clone https://github.com/tu_usuario/aprende-ingles-jugando.git
Instala las dependencias necesarias:
pip install -r requirements.txt
Configuración:

Configura tus credenciales de AWS en el archivo .env:
AWS_ACCESS_KEY_ID=<tu_clave>
AWS_SECRET_ACCESS_KEY=<tu_secreto>
AWS_REGION=<tu_región>
Ejecutar la aplicación:

Inicia la aplicación localmente:
python app.py
Accede en tu navegador en http://localhost:5000.


📈 Roadmap
Mejorar la experiencia del juego con puntuaciones y niveles.
Integrar una función de estadísticas para seguir tu progreso.
Añadir más tipos de ejercicios, como completar frases o dictados.
📝 Contribuciones
¡Todas las ideas son bienvenidas! Si quieres colaborar:

Haz un fork del repositorio.
Crea una rama para tu funcionalidad:
git checkout -b nueva-funcionalidad
Envía tu pull request.
🖥️ Autor
Desarrollado con ❤️ por Francisco.
