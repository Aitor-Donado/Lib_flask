# app_plantillas.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('base.html')

@app.route('/usuario/<nombre>')
def perfil(nombre):
    return render_template('perfil.html',
                          nombre=nombre,
                          activo=True,
                          habilidades=['Python', 'Flask', 'HTML'])

if __name__ == '__main__':
    app.run(debug=True)