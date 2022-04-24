from sqlalchemy import create_engine

from scripts.seed import get_database_path


db = create_engine('sqlite:////{}'.format(get_database_path('github_users.db')))