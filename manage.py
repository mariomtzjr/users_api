from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from main import app
from app.main.database import db


app.app_context().push()
migrate = Migrate(app, db)
manager = Manager(app)

try:
    manager.add_command('db', MigrateCommand)
except Exception as e:
    print("Migrations already created: {}".format(e))
    pass


@manager.command
def run():
    app.run(host="0.0.0.0", port=8000)


if __name__ == '__main__':
    manager.run()