# app_basico.py
from flask import Flask

# Crear aplicación Flask
app = Flask(__name__)
import os
app.secret_key = os.environ.get('SECRET_KEY')

# Ruta básica
@app.route('/')
def hola_mundo():
    return '<h1>¡Hola Mundo desde Flask!</h1>'

# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)