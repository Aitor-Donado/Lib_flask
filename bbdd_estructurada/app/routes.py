from flask import Blueprint, render_template
from .models import Post, User  # Importa tus modelos
from .extensions import db

# Crea un Blueprint para las rutas principales
main_bp = Blueprint('main', __name__)

# Ruta de ejemplo (página de inicio)
@main_bp.route('/')
def index():
    return "¡Hola Mundo! Esta es la página principal."

# Ruta de ejemplo con base de datos (lista de posts)
@main_bp.route('/posts')
def list_posts():
    posts = Post.query.all()  # Consulta todos los posts
    return render_template('posts.html', posts=posts)

# (Opcional) Ruta para crear un post de ejemplo (solo para pruebas)
@main_bp.route('/create_test_post')
def create_test_post():
    # Verifica si existe un usuario de prueba
    user = User.query.filter_by(username='test_user').first()
    if not user:
        # Crea un usuario de prueba si no existe
        user = User(username='test_user', email='test@example.com')
        db.session.add(user)
        db.session.commit()

    # Crea un post de prueba
    new_post = Post(
        title='Post de prueba',
        content='Este es un post creado automáticamente.',
        author_id=user.id
    )
    db.session.add(new_post)
    db.session.commit()

    return "¡Post de prueba creado!"