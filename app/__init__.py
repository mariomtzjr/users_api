from flask import Flask

from app.database import db


def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)
    
    # Inicializa las extensiones
    db.init_app(app)

    return app