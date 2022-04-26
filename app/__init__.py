import os
import sqlite3

from flask import Flask, jsonify
from flask_restful import Api

from app.ext import ma, migrate
from app.resources import users_blueprint
from app.main.database import db


def create_app(settings_module):
    app = Flask(__name__, template_folder='app/templates/')
    
    app.config.from_object(settings_module)
    app.register_blueprint(users_blueprint)

    print("db: ", db)
    

    # Captura todos los errores 404
    Api(app, catch_all_404s=True)

    # Deshabilita el modo estricto de acabado de una URL con /
    app.url_map.strict_slashes = False

 
    return app