import os
import sys
import platform
from flask import Blueprint
from flask import current_app as app, request
from werkzeug.datastructures import CombinedMultiDict
from apps.admin.forms import UploadForm
import string
import time
import random
import hashlib
from exts import db
from apps.admin.models import File

bp = Blueprint('uploader',__name__,url_prefix='/uploader')

if platform.system() == "Windows":
    slash='\\'
else:
    slash = '/'

UPLOAD_IMAGES_PATH = ''


@bp.before_app_first_request
def before_first_request():
    global UPLOAD_IMAGES_PATH

    UPLOAD_IMAGES_PATH = app.config.get('UPLOAD_IMAGES_PATH')
    if UPLOAD_IMAGES_PATH and not os.path.exists(UPLOAD_IMAGES_PATH):
        os.mkdir(UPLOAD_IMAGES_PATH)

    csrf = app.extensions.get('csrf')
    if csrf == 1:
        csrf.exempt(upload)


def _random_filename(rawfilename):
    letters = string.ascii_letters
    random_filename = str(time.time()) + "".join(random.sample(letters, 5))
    filename = hashlib.md5(random_filename.encode('utf8')).hexdigest()
    subffix = rawfilename.rsplit('.',1)[1]
    return filename + '.' + subffix


@bp.route('/upload',methods=['POST'])
def upload():
    if request.method == 'POST':
        form = UploadForm(CombinedMultiDict([request.form,request.files]))
        if form.validate():
            file = request.files['file']
            filename=file.filename
            save_filename=_random_filename(filename)
            file.save(os.path.join(UPLOAD_IMAGES_PATH,save_filename))
            f=File(name=filename,path=save_filename)
            db.session.add(f)
            db.session.commit()
            return '上传文件成功！'
        else:
            return form.errors
