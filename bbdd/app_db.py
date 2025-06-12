# app_db.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

# Modelo de datos
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.Text, nullable=False)

# Crear las tablas (solo se ejecuta una vez)
with app.app_context():
    db.create_all()


@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    if request.method == "POST":
        titulo = request.form["titulo"]
        contenido = request.form["contenido"]
        nuevo_post = Post(titulo=titulo, contenido=contenido)
        db.session.add(nuevo_post)
        db.session.commit()
        return redirect(url_for('listar_posts'))
    else:
        return render_template("nuevo.html")


@app.route('/posts')
def listar_posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)