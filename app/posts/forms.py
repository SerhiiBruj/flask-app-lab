from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, SelectField, DateTimeLocalField
from wtforms.validators import DataRequired, Length
from datetime import datetime as dt
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=255)])
    body = TextAreaField('body', validators=[DataRequired()])
    publish_date = DateTimeLocalField('Publish Date', format='%Y-%m-%dT%H:%M', validators=[DataRequired()],default=dt.now)
    category = SelectField('Category', choices=[('tech', 'Tech'), ('other', 'Other')], validators=[DataRequired()])
    author = TextAreaField('author',default='Anonymous', validators=[Length(max=20)])
    submit = SubmitField('Submit')
