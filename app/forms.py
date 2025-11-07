from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField(
        'Ім’я',
        validators=[DataRequired(message="Поле обов’язкове"), Length(min=2, max=50)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(message="Поле обов’язкове"), Email(message="Некоректна адреса email")]
    )
    message = TextAreaField(
        'Повідомлення',
        validators=[DataRequired(message="Введіть повідомлення"), Length(min=5)]
    )
    submit = SubmitField('Надіслати')
