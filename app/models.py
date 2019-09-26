from datetime import datetime
from app import create_app
from app import db

class User(db.Model):
    id = db.column(db.Integer, primary_key = True)
    phone_number = db.column(db.Integer, unique=True, nullable=False)
    username = db.column(db.String(20), unique=True, nullable=False)
    email = db.column(db.String(20), unique=True, nullable=False)
    pasword = db.column(db.String(60), unique=True, nullable=False)
    # uploads = db.relationship('Upload_Item', backref='owner', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# class Upload_Item(db.Model):
#     id = db.column(db.Integer, primary_key = True)
#     title = db.column(db.String(20), unique=True, nullable=False)
#     author = db.column(db.String(20), unique=True, nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     category = db.column(db.String(20), unique=True, nullable=False)
#     quantity = db.column(db.Int(20), unique=True, nullable=False)
#     price = db.column(db.Int(20), unique=True, nullable=False)
#     user_id = db.Coluimn(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return f"Product('{self.title}', '{self.author}', '{self.date_posted}', '{self.quantity}', '{self.price}')"

