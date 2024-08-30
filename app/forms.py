from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class URLForm(FlaskForm):
    original_url = StringField('Original URL', validators=[DataRequired(), URL()])
    submit = SubmitField('Shorten')