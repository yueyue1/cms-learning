import os
SECRET_KEY = os.urandom(24)

DB_USERNAME = 'root'
DB_PASSWORD = 'zKartCvauO42Mo8fX7al7pBd79FCbEml'
DB_HOST = '139.199.209.220'
DB_PORT = 3306
DB_DATABASE = 'kyra_appletest'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
FLASK_DB_QUERY_TIMEOUT = 0.05
ADMIN_USER_ID = 'CMSKYRA'

UPLOAD_IMAGES_PATH = os.path.join(os.path.dirname(__file__),'upload','images')