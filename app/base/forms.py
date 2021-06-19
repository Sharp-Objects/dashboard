# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present SharpObjects
"""

from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import Email, DataRequired


## login and registration

class LoginForm(FlaskForm):
    username = TextField('Имя', id='username_login', validators=[DataRequired()])
    password = PasswordField('Пароль', id='pwd_login', validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = TextField('Имя', id='username_create', validators=[DataRequired()])
    email = TextField('Почта', id='email_create', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', id='pwd_create', validators=[DataRequired()])
