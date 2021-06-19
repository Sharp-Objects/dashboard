# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present SharpObjects
"""
from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String, TIMESTAMP

from app import db, login_manager
from app.base.util import hash_pass


class Common(db.Model, UserMixin):
    __tablename__ = 'Common'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())
    model_name = Column(String, unique=False)
    high_value = Column(Integer)
    low_value = Column(Integer)
    pulse = Column(Integer)
    activity = Column(String(256), nullable=True)

    def __init__(self, **kwargs):
        print(kwargs.items())
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]
            setattr(self, property, value)

    def __repr__(self):
        return f"{str(self.high_value)}/{str(self.low_value)}"


class User(db.Model, UserMixin):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(Binary)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            if hasattr(value, '__iter__') and not isinstance(value, str):
                value = value[0]
            if property == 'password':
                value = hash_pass(value)
            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)


class Patient(db.Model):
    __tablename__ = 'Patient'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    gender = Column(String)
    age = Column(Integer)
    birth_date = Column(String)

    # birth_date = datetime.strptime(birth_date, "%Y/%M/%d")


@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None
