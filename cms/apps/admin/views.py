from flask import Blueprint,render_template, send_from_directory,request,jsonify
import os
from exts import db
from .models import File
from .recursion import create_file_list
import config

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
def hello():
    return render_template('admin/index.html')


@bp.route('/file_down',methods=['GET'])
def file_down():
    fid = request.args.get('id')
    file = File.query.filter(File.fid == fid).first()
    return send_from_directory(config.UPLOAD_IMAGES_PATH,file.path,as_attachment=True)


@bp.route('/file_list',methods=['GET'])
def file_list():
    files = db.session.query(File).all()
    list = create_file_list(files)
    return render_template('admin/file_list.html',message=list)


@bp.route('/file_del',methods=['POST'])
def file_del():
    if request.method == 'POST':
        id = request.values.get('id')
        file = File.query.filter(File.fid == id).first()
        result = {}
        if file:
            path = file.path
            try:
                os.remove(os.path.join(config.UPLOAD_IMAGES_PATH,path))
            except:
                print('文件不存在，位置', os.path.join(config.UPLOAD_IMAGES_PATH,path))
            db.session.delete(file)
            db.session.commit()
            result = {
                'status': 200,
                'msg': '成功'
            }
            return jsonify(result)
        else:
            result = {
                'status': 202,
                'msg': '文件不存在'
            }
            return jsonify(result)
