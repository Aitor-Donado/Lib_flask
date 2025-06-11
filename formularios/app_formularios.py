# app_formularios.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        # Procesar datos (ej. guardar en DB)
        return f'¡Registro exitoso, {nombre}!'
    return render_template('registro.html')

# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)