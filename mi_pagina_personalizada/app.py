from flask import Flask, render_template
from flask import request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'


@app.route('/')
def inicio():
    return render_template("inicio.html", color_fondo="lightblue")

@app.route('/configurar', methods=['GET', 'POST'])
def configurar():
    if request.method == 'POST':
        # Aquí puedes agregar la lógica para guardar los cambios
        print("request.form: ", request.form)
        return redirect(url_for('inicio'))
    # Aquí puedes agregar la lógica para obtener los valores actuales de la configuración
    return render_template("configurar.html")

if __name__ == '__main__':
    app.run(debug=True)