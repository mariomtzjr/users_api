from flask_sqlalchemy import SQLAlchemy

from scripts.seed import get_database_path
from main import app

db = SQLAlchemy(app)