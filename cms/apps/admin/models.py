from exts import db
from werkzeug.security import generate_password_hash, check_password_hash


class Users(db.Model):
    __tablename__='ky_user'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False,unique=True)
    _password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

    @property
    def password(self):
        return self._password


    @password.setter
    def password(self,raw_password):
        self._password = generate_password_hash(raw_password)


    def check_password(self,raw_password):
        return check_password_hash(self._password,raw_password)


    __table_args__={
        'mysql_charset': 'utf8'
    }

class File(db.Model):
    __tablename__='ky_files'
    fid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200),nullable=False)
    path = db.Column(db.String(800),nullable=False)

    __table_args__={
        'mysql_charset': 'utf8'
    }
