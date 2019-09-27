from datetime import datetime
from flask import current_app
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.phone_number}', '{self.username}' , '{self.email}')"