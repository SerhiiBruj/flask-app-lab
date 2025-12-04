from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, SelectField, DateTimeLocalField
from wtforms.validators import DataRequired, Length
from datetime import datetime as dt



from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired
from app.posts.models import Tag

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=255)])
    body = TextAreaField('body', validators=[DataRequired()])
    publish_date = DateTimeLocalField('Publish Date', format='%Y-%m-%dT%H:%M', validators=[DataRequired()],default=dt.now)
    category = SelectField('Category', choices=[('tech', 'Tech'), ('other', 'Other')], validators=[DataRequired()])
    tags = SelectMultipleField("Tags", coerce=int) 
    author = SelectField('Author', choices=[(1, 1),(2,2)])  
    submit = SubmitField('Submit')
    def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            # Підвантажуємо всі теги з БД у choices
            self.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by(Tag.name).all()]
    def set_tag_choices(self):
        self.tags.choices = [(tag.id, tag.name) for tag in Tag.query.all()]
    
    