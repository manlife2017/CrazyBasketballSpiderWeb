# -*- coding:utf-8 -*-
from flask_script import Manager, prompt_bool
from application import app, db
from flask_migrate import Migrate, MigrateCommand
from models import UserModel

app = app.app
db = db.db
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

if __name__ == "__main__":
    manager.run()