from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_by_name

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    with app.app_context():
        from .routes import main_bp
        app.register_blueprint(main_bp)
        db.create_all()

    return app
