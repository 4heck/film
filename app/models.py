from app import db
import re

class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def to_dict(self):
        dict = {
        'name': self.name,
        }
        return dict

class Size(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def to_dict(self):
        dict = {
        'name': self.name,
        }
        return dict

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.Integer)
    size = db.Column(db.Integer)
    price = db.Column(db.Integer)
    coffee = db.Column(db.Integer)
    milk = db.Column(db.Integer)
    creammilk = db.Column(db.Integer)
    chocolate_topping = db.Column(db.Integer)
    syrup = db.Column(db.Integer)
    chocolate = db.Column(db.Integer)
    cocoa = db.Column(db.Integer)
    icecream = db.Column(db.Integer)
    tea = db.Column(db.Integer)
    cup_espresso = db.Column(db.Integer)
    cup_small = db.Column(db.Integer)
    cup_middle = db.Column(db.Integer)
    cup_big = db.Column(db.Integer)

    def to_dict(self):
        dict = {
        'name': self.name,
        'type': self.type,
        'size': self.size,
        'price': self.price,
        'coffee': self.coffee,
        'milk': self.milk,
        'creammilk': self.creammilk,
        'chocolate_topping': self.chocolate_topping,
        'syrup': self.syrup,
        'chocolate': self.chocolate,
        'cocoa': self.cocoa,
        'icecream': self.icecream,
        'tea': self.tea,
        'cup_espresso': self.cup_espresso,
        'cup_small': self.cup_small,
        'cup_middle': self.cup_middle,
        'cup_big': self.cup_big,
        }
        return dict

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coffee = db.Column(db.Integer)
    milk = db.Column(db.Integer)
    creammilk = db.Column(db.Integer)
    chocolate_topping = db.Column(db.Integer)
    syrup = db.Column(db.Integer)
    chocolate = db.Column(db.Integer)
    cocoa = db.Column(db.Integer)
    icecream = db.Column(db.Integer)
    tea = db.Column(db.Integer)
    cup_espresso = db.Column(db.Integer)
    cup_small = db.Column(db.Integer)
    cup_middle = db.Column(db.Integer)
    cup_big = db.Column(db.Integer)
    thermoglass1 = db.Column(db.Integer)
    wooden_icon1 = db.Column(db.Integer)
    wooden_icon2 = db.Column(db.Integer)
    coffee_250gr = db.Column(db.Integer)
    postcard = db.Column(db.Integer)
    chips_with_basil = db.Column(db.Integer)
    chips_with_banana = db.Column(db.Integer)
    chips_with_orange = db.Column(db.Integer)
    chips_with_fruit_mix = db.Column(db.Integer)
    chips_with_pinapple = db.Column(db.Integer)
    chips_with_watermelon = db.Column(db.Integer)
    chips_with_mango = db.Column(db.Integer)
    chips_with_pear = db.Column(db.Integer)
    chips_with_cocos = db.Column(db.Integer)
    chips_with_melon = db.Column(db.Integer)
    sandwich_with_chicken = db.Column(db.Integer)
    protein_snack = db.Column(db.Integer)
    muffin = db.Column(db.Integer)
    donut = db.Column(db.Integer)
    cookie = db.Column(db.Integer)
    fruit_snack = db.Column(db.Integer)
    macarons = db.Column(db.Integer)
    wagon_wheels = db.Column(db.Integer)
    nutella = db.Column(db.Integer)
    mini_ritter_sport = db.Column(db.Integer)

    def to_dict(self):
        dict = {
        'coffee': self.coffee,
        'milk': self.milk,
        'creammilk': self.creammilk,
        'chocolate_topping': self.chocolate_topping,
        'syrup': self.syrup,
        'chocolate': self.chocolate,
        'cocoa': self.cocoa,
        'icecream': self.icecream,
        'tea': self.tea,
        'cup_espresso': self.cup_espresso,
        'cup_small': self.cup_small,
        'cup_middle': self.cup_middle,
        'cup_big': self.cup_big,
        'thermoglass1': self.thermoglass1,
        'wooden_icon1': self.wooden_icon1,
        'wooden_icon2': self.wooden_icon2,
        'coffee_250gr': self.coffee_250gr,
        'postcard': self.postcard,
        'chips_with_basil': self.chips_with_basil,
        'chips_with_banana': self.chips_with_banana,
        'chips_with_orange': self.chips_with_orange,
        'chips_with_fruit_mix': self.chips_with_fruit_mix,
        'chips_with_pinapple': self.chips_with_pinapple,
        'chips_with_watermelon': self.chips_with_watermelon,
        'chips_with_mango': self.chips_with_mango,
        'chips_with_pear': self.chips_with_pear,
        'chips_with_cocos': self.chips_with_cocos,
        'chips_with_melon': self.chips_with_melon,
        'sandwich_with_chicken': self.sandwich_with_chicken,
        'protein_snack': self.protein_snack,
        'muffin': self.muffin,
        'donut': self.donut,
        'cookie': self.cookie,
        'fruit_snack': self.fruit_snack,
        'macarons': self.macarons,
        'wagon_wheels': self.wagon_wheels,
        'nutella': self.nutella,
        'mini_ritter_sport': self.mini_ritter_sport,
        }
        return dict