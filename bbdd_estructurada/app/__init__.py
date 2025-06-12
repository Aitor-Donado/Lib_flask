# app/__init__.py
from flask import Flask
from .extensions import db, migrate

def create_app(config_class='instance.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app