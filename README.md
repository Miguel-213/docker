# ☕ Café Aurora

Café Aurora es una aplicación web desarrollada con **Flask**, que muestra la página de ejemplo de una cafetería artesanal.  
El proyecto está diseñado para ejecutarse dentro de un contenedor **Docker**, exponiendo la aplicación en el puerto **80**.

---
## Para poder usar el docker

Es necesario para poder usar el docker descargar los archivos correspondientes y tener instalado el flask y el docker

```bash
sudo apt install python3.12 -y
sudo apt install python3-pip -y
sudo apt install python3-flask -y 
```

## 🧩 Estructura del proyecto

app/

├── main.py

├── Dockerfile

└── README.md


### 1. Construir la imagen

Desde la carpeta del proyecto:

```bash
sudo docker build . -t web:01
sudo docker run -d -p 80:80 web:01 
```
#Abrir el navegador

Tras esto es importante desplazarte a la parte del navegador e ingresar tu direccion ip seguida de el puerto que se este uisando en este caso el 80
