from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        from models import init_db
        init_db()  # Crea las tablas si no existen

        from routes.routes import user_bp
        app.register_blueprint(user_bp, url_prefix='/users')

    return app
