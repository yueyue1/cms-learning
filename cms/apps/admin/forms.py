from flask_wtf.file import FileAllowed,FileRequired
from wtforms import Form, FileField,StringField
from wtforms.validators import InputRequired

class UploadForm(Form):
    file = FileField(validators=[FileRequired(),FileAllowed(['jpg','png','gif','txt'])])

class LoginForm(Form):
    username = StringField(validators=[InputRequired('必须填写')])
    password = StringField(validators=[InputRequired('必须填写')])