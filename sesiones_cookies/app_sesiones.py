# app_sesiones.py
from flask import Flask, session, redirect, url_for, render_template, request

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Necesaria para sesiones

@app.route('/')
def inicio():
    return render_template('base.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Aquí iría la lógica de autenticación
        print(request.form)
        print(request.user_agent)
        session['usuario'] = request.form.get('username')
        session['user_agent'] = request.user_agent.string
        session['ip_address'] = request.remote_addr
        return redirect(url_for('perfil'))
    return render_template('login.html')

@app.route('/perfil')
def perfil():
    if 'usuario' in session:
        return render_template('perfil.html', usuario=session['usuario'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

from flask import make_response

@app.route('/setcookie')
def set_cookie_route():
    # Suponiendo que tienes una plantilla base.html o similar
    resp = make_response(render_template('base.html')) # O simplemente make_response("Cookie establecida!")
    if 'usuario' in session:
        resp.set_cookie('username', session['usuario'])
    else:
        resp.set_cookie('username', 'invitado')
    resp.set_cookie('preferenciaColor', 'azul', max_age=60*60*24*30) # max_age en segundos (aquí 30 días)
    return resp

@app.route('/getcookie')
def get_cookie_route():
    username = request.cookies.get('username')
    if username:
        return f'Cookie username: {username}'   
    else:
        return 'No se encontró la cookie'

if __name__ == '__main__':
    app.run(debug=True)