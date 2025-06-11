# blog/routes.py
from flask import Blueprint

blog_bp = Blueprint('blog', __name__, template_folder='templates')

@blog_bp.route('/post/<int:id>')
def ver_post(id):
    return f'Viendo post {id}'