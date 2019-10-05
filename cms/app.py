from flask import Flask
from exts import db
from apps.admin.views import bp as admin_bp
from apps.front.views import bp as front_bp
from apps.uploader import bp as upload_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(admin_bp)
    app.register_blueprint(front_bp)
    app.register_blueprint(upload_bp)
    app.config.from_object('config')
    db.init_app(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0',port=80)