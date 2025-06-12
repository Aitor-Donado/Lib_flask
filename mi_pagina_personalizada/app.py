from flask import Flask, render_template, session, make_response
from flask import request, redirect, url_for
from flask_wtf import FlaskForm, CSRFProtect


app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'
csrf = CSRFProtect(app)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/configurar', methods=['GET', 'POST'])
def configurar():
    if request.method == 'POST':
        # Aquí puedes agregar la lógica para guardar los cambios
        print("request.form: ", request.form)
        session["usuario"] = request.form["nombre"]
        color_elegido = request.form["color"]
        response = make_response(redirect(url_for('inicio')))
        response.set_cookie('color_fondo', color_elegido)
        return response

    # Aquí puedes agregar la lógica para obtener los valores actuales de la configuración
    return render_template("configurar.html")

@app.route('/olvidar')
def olvidar():
    session.pop('usuario', None)
    response = make_response(redirect(url_for('inicio')))
    response.delete_cookie('color_fondo')
    return response

if __name__ == '__main__':
    app.run(debug=True)