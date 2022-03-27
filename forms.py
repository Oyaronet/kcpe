from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                 Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(),
                 Length(min=8, max=60)])
    password = PasswordField('Password', validators=[DataRequired(),
                 Length(min=4, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
                 Length(min=4, max=20), EqualTo('password')])
    register = SubmitField('REGISTER')


class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                 Length(min=8, max=60)])
    password = PasswordField('Password', validators=[DataRequired(),
                 Length(min=4, max=20)])
    login = SubmitField('LOG IN')

class AdminLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
                 Length(min=8, max=60)])
    password = PasswordField('Password', validators=[DataRequired(),
                 Length(min=4, max=20)])
    login = SubmitField('LOG IN')