from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'


@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/configurar')
def configurar():
    return render_template("configurar.html")

if __name__ == '__main__':
    app.run(debug=True)