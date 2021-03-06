# -*- coding: utf8 -*-

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from src.app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
# db.create_all()

if __name__ == '__main__':
    manager.run()
