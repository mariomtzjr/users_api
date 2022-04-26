import os
import sqlite3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from app.resources import users_blueprint


ma = Marshmallow()
migrate = Migrate()


def create_app(settings_module):
    app = Flask(__name__, template_folder='app/templates/')
    app.config.from_object(settings_module)
    app.register_blueprint(users_blueprint)
    
    db = SQLAlchemy(app)

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
    
    # Captura todos los errores 404
    Api(app, catch_all_404s=True)

    # Deshabilita el modo estricto de acabado de una URL con /
    app.url_map.strict_slashes = False

 
    return app