from flask_login import UserMixin
from app.config import db


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(500))
    searchhistory = db.relationship('SearchHistory', backref='users', uselist=False)


class SearchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    temp_in_c = db.Column(db.String(30), nullable=False)
    temp_in_f = db.Column(db.String(30), nullable=False)
    times = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
