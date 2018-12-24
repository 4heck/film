from app import db
import re

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def to_dict(self):
        dict = {
        'name': self.name,
        }
        return dict

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def to_dict(self):
        dict = {
        'name': self.name,
        }
        return dict

class Deal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(100))
    customer = db.Column(db.String(100))
    car = db.Column(db.String(100))

    def to_dict(self):
        dict = {
        'owner': self.owner,
        'customer': self.customer,
        'car': self.car
        }
        return dict

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.String(100))
    year = db.Column(db.String(100))
    mileage = db.Column(db.String(100))

    def to_dict(self):
        dict = {
        'name': self.name,
        'price': self.price,
        'year': self.year,
        'mileage': self.mileage
        }
        return dict