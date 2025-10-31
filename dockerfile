# Imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo principal
COPY main.py .

# Instalar Flask
RUN pip install flask

# Exponer el puerto 5000
EXPOSE 80

# Comando para ejecutar la app
CMD ["python", "main.py"]

