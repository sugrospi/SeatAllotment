
# models.py

from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(100))
  name = db.Column(db.String(1000))
  rank = db.Column(db.Integer,unique = True)
  C1 = db.Column(db.Integer)
  C2 = db.Column(db.Integer)
  C3 = db.Column(db.Integer)
