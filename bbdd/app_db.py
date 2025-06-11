# app_db.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

# Modelo de datos
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.Text, nullable=False)

@app.route('/posts')
def listar_posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)