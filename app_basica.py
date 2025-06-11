# app_basico.py
from flask import Flask

# Crear aplicación Flask
app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_muy_compleja_aqui'

# Ruta básica
@app.route('/')
def hola_mundo():
    return '<h1>¡Hola Mundo desde Flask!</h1>'

# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)