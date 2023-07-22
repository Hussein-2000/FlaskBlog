from flask_sqlalchemy import SQLAlchemy as sq
from app import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = sq(app)



# #models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    gender = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)



class students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(100), nullable=False)
    LasttName = db.Column(db.String(100), nullable=False)
    midletName = db.Column(db.String(100), nullable=False)
    motherName = db.Column(db.String(100), nullable=False)
    dateOfBirth = db.Column(db.DateTime, nullable=False)
    placeOfBirth = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

