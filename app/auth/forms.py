from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired, Length(1, 64),
                                             Email])
    password = PasswordField('Password', validators=[DataRequired])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class SignUp(FlaskForm):
    email = StringField('Email', validators=[DataRequired, Length(1, 64),
                                             Email])
    password = PasswordField('Password', validators=[DataRequired])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign up')
