from flask import Flask, render_template

app = Flask(__name__)

@app.route('/con-estilo')
def pagina_con_estilo():
    return render_template('mi_pagina.html')

if __name__ == '__main__':
    app.run(debug=True)