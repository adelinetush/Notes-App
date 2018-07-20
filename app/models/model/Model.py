from app.models import BaseModel
from app.models import db
from app import app
from flask_sqlalchemy import SQLAlchemy
import datetime
from passlib.apps import custom_app_context as pwd_context


class User(BaseModel,db.Model):
    '''base initizialization function'''
    __tablename__ = "User"

    id  = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(32),index=True)
    password = db.Column(db.String(128))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.password = password
        #self.password_hash  = self.hash_password(password)
        #self.password = self.hash_password(password)

    def __str__(self): 
            return "User(id='%s')" % self.id

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
        return self.password_hash

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    def serialize(self):
            
            return {
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'password':self.password
            }

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user

class Entry(BaseModel, db.Model):
    __tablename__ = "Entry"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    title = db.Column(db.String(120))
    notes = db.Column(db.String(500))
    date = db.Column(db.String(120))

    def __init__(self, email, title, notes, date):
        self.email = email;
        self.title = title
        self.notes = notes 
        self.date = date      


    def serialize(self):
            return {
            'id':self.id,
            'email':self.email,
            'title':self.title,
            'notes':self.notes,
            'date':self.date
    }