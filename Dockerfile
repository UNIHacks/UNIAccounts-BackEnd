# Usamos una imagen base con Python
FROM python:3.9

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos los archivos de la aplicación a la imagen
COPY ./src /app
COPY ./requirements/local.txt /app/requirements.txt

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Definimos el puerto en el que se ejecutará la aplicación Flask
EXPOSE 5000

# Comando para ejecutar la aplicación Flask y especificar el archivo principal
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]


