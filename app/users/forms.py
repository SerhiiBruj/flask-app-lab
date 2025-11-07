from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("Username / Email", validators=[DataRequired(message="Поле обов'язкове!")])
    password = PasswordField("Пароль", validators=[
        DataRequired(message="Поле обов'язкове!"),
        Length(min=4, max=10, message="Пароль має бути від 4 до 10 символів!")
    ])
    remember = BooleanField("Запам'ятати мене")
    submit = SubmitField("Увійти")
