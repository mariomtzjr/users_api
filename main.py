import os

from flask import Flask, render_template, Blueprint

from app import create_app
from app.resources import users_blueprint

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)