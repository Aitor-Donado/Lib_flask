# app_rutas.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Página de inicio'

# Ruta con parámetro string
@app.route('/usuario/<username>')
def perfil_usuario(username):
    return f'Perfil de {username}'

# Ruta con parámetro numérico
@app.route('/post/<int:post_id>')
def mostrar_post(post_id):
    return f'Post #{post_id}'

# Ruta múltiples parámetros
@app.route('/producto/<categoria>/<int:producto_id>')
def producto(categoria, producto_id):
    return f'Categoría: {categoria}, Producto ID: {producto_id}'

if __name__ == '__main__':
    app.run(debug=False)
