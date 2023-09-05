# Tunevault

Django corre en un virtual environment

Instalar localmente env

``pip install pipenv``

Crear virtual environment

``python3 -m venv venv``

En el virtual environment se van a instalar el resto de las librerias necesarias
- ``pip install django``
- ``pip install react``

Para acceder al virtual environment: ``source venv/bin/activate``

Comandos utiles para Django
- ``python manage.py runserver`` -> para correrlo (importante, tenes que estar en /backend)
- ``python manage.py runmigrations`` y despues ``python manage.py migrate`` cuando se crean nuevos Models (tienen que ver con las BD)

Comandos utiles para React
- ``npm start`` -> para correrlo (importante, tenes que estar en /frontend)

Nota: no se por que pero a veces no anda con python pero si poniendo python3, lo mismo pasa con pip y pip3

