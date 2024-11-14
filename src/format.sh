#!/bin/bash

# Muestra un mensaje antes de ejecutar Flake8
echo "Ejecutando Flake8..."

# Navega al directorio donde se encuentra el archivo config.ini
cd utilities/

# Ejecuta Flake8 con la configuración del archivo config.ini
flake8 --config=config.ini

# Formatea el código Python usando Black
black .

# Muestra un mensaje después de ejecutar Flake8 y Black
echo "Flake8 y Black finalizados."