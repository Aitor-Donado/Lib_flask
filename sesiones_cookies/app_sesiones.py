# app_sesiones.py
from flask import Flask, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Necesaria para sesiones

@app.route('/login')
def login():
    session['usuario'] = 'Ana'
    return 'Sesión iniciada'

@app.route('/perfil')
def perfil():
    if 'usuario' in session:
        return f'Bienvenida {session["usuario"]}'
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return 'Sesión cerrada'

if __name__ == '__main__':
    app.run(debug=True)