# ramsa_project



## Ejecución con Entorno Virtual

### Requisitos

- Python 3.9.0+
- pip (instalador de paquetes de Python)

### Pasos

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/zlterry68/ramsa_project.git

2. Navega al directorio de la aplicación:
    cd ramsa_project


3. Crea y activa un entorno virtual:
    python3 -m venv venv
    source venv/bin/activate

4. Instala las dependencias del proyecto:
    pip install -r requirements.txt


5. Ejecuta la aplicación:
    uvicorn main:app --reload


6. Abre tu navegador web y navega a http://127.0.0.1:8000 para ver la aplicación en funcionamiento.

## Ejecución con Docker

### Requisitos

- Docker

### Pasos

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/zlterry68/ramsa_project.git


2. Navega al directorio de la aplicación:

    cd ramsa_project


3. Construye la imagen de Docker:

    docker build -t mi-aplicacion .


4. Ejecuta el contenedor Docker:


    docker run -d -p 8000:8000 mi-aplicacion

5. Abre tu navegador web y navega a http://127.0.0.1:8000 para ver la aplicación en funcionamiento.

