from flask_wtf.file import FileAllowed,FileRequired
from wtforms import Form, FileField

class UploadForm(Form):
    file = FileField(validators=[FileRequired(),FileAllowed(['jpg','png','gif','txt'])])