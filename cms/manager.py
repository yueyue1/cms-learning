from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from exts import db
from app import create_app
from apps.admin import models as admin_models


app = create_app()
Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)


@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
@manager.option('-e','--email', dest='email')
def create_user(username, password, email):
    user = admin_models.Users(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    manager.run()