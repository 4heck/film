from app import app
from models import Type
from models import Size
from models import Product
from models import Stock
from flask import jsonify
from flask import request
from app import db
import json

#api's for TYPE
@app.route('/api/type', methods=['GET'])
def api_type_get():
    types = Type.query.all()
    types_json = [{"id": type.id, "name": type.name}
                  for type in types]
    return jsonify(types_json)

@app.route('/api/type/<id>', methods=['GET'])
def api_type_get_id(id):
    types = Type.query.filter_by(id=id)
    if not types:
        abort(404)
    type = types[0]
    type_json = {"id": type.id, "name": type.name}
    return jsonify(type_json)

@app.route('/api/type', methods=['POST'])
def api_type_insert():
    new_type = request.get_json()
    type = Type(id=new_type['id'], name=new_type['name'])
    db.session.add(type)
    db.session.commit()
    type_json = {"id": type.id, "name": type.name}
    return jsonify(type_json)

@app.route('/api/type/<id>', methods=['DELETE'])
def api_type_delete(id):
    types = Type.query.filter_by(id=id)
    if not types:
        abort(404)
    type = types[0]
    db.session.delete(type)
    db.session.commit()
    return jsonify()

@app.route('/api/type/<id>', methods=['PUT'])
def api_type_update(id):
    updated_type = request.get_json()
    types_to_update = Type.query.filter_by(id=id)
    data = json.loads(request.get_data())
    type_to_update = types_to_update[0]
    type_to_update = db.session.query(Type).filter_by(id = id).first()
    type_to_update.name = data['name']
    db.session.commit()
    return jsonify(type_to_update.to_dict())

#api's for SIZE
@app.route('/api/size', methods=['GET'])
def api_size_get():
    sizes = Size.query.all()
    sizes_json = [{"id": size.id, "name": size.name}
                  for size in sizes]
    return jsonify(sizes_json)

@app.route('/api/size/<id>', methods=['GET'])
def api_size_get_id(id):
    sizes = Size.query.filter_by(id=id)
    if not sizes:
        abort(404)
    size = sizes[0]
    size_json = {"id": size.id, "name": size.name}
    return jsonify(size_json)

@app.route('/api/size', methods=['POST'])
def api_size_insert():
    new_size = request.get_json()
    size = Size(id=new_size['id'], name=new_size['name'])
    db.session.add(size)
    db.session.commit()
    size_json = {"id": size.id, "name": size.name}
    return jsonify(size_json)

@app.route('/api/size/<id>', methods=['DELETE'])
def api_size_delete(id):
    sizes = Size.query.filter_by(id=id)
    if not sizes:
        abort(404)
    size = sizes[0]
    db.session.delete(size)
    db.session.commit()
    return jsonify()

@app.route('/api/size/<id>', methods=['PUT'])
def api_size_update(id):
    updated_size = request.get_json()
    sizes_to_update = Size.query.filter_by(id=id)
    data = json.loads(request.get_data())
    size_to_update = sizes_to_update[0]
    size_to_update = db.session.query(Size).filter_by(id = id).first()
    size_to_update.name = data['name']
    db.session.commit()
    return jsonify(size_to_update.to_dict())

#api's for PRODUCT
@app.route('/api/product', methods=['GET'])
def api_product_get():
    products = Product.query.all()
    products_json = [{"id": product.id, "name": product.name, "type": product.type, "size": product.size, "price": product.price, "coffee": product.coffee, "milk": product.milk, "creammilk": product.creammilk, "chocolate_topping": product.chocolate_topping, "syrup": product.syrup, "chocolate": product.chocolate, "cocoa": product.cocoa, "icecream": product.icecream, "tea": product.tea, "cup_espresso": product.cup_espresso, "cup_small": product.cup_small, "cup_middle": product.cup_middle, "cup_big": product.cup_big}
                  for product in products]
    return jsonify(products_json)

@app.route('/api/product/<id>', methods=['GET'])
def api_product_get_id(id):
    products = Product.query.filter_by(id=id)
    if not products:
        abort(404)
    product = products[0]
    product_json = {"id": product.id, "name": product.name, "type": product.type, "size": product.size, "price": product.price, "coffee": product.coffee, "milk": product.milk, "creammilk": product.creammilk, "chocolate_topping": product.chocolate_topping, "syrup": product.syrup, "chocolate": product.chocolate, "cocoa": product.cocoa, "icecream": product.icecream, "tea": product.tea, "cup_espresso": product.cup_espresso, "cup_small": product.cup_small, "cup_middle": product.cup_middle, "cup_big": product.cup_big}
    return jsonify(product_json)

@app.route('/api/product', methods=['POST'])
def api_product_insert():
    new_product = request.get_json()
    product = Product(id=new_product['id'], name=new_product['name'], type=new_product['type'], size=new_product['size'], price=new_product['price'], coffee=new_product['coffee'], milk=new_product['milk'], creammilk=new_product['creammilk'], chocolate_topping=new_product['chocolate_topping'], syrup=new_product['syrup'], chocolate=new_product['chocolate'], cocoa=new_product['cocoa'], icecream=new_product['icecream'], tea=new_product['tea'], cup_espresso=new_product['cup_espresso'], cup_small=new_product['cup_small'], cup_middle=new_product['cup_middle'], cup_big=new_product['cup_big'])
    db.session.add(product)
    db.session.commit()
    product_json = {"id": product.id, "name": product.name, "type": product.type, "size": product.size, "price": product.price, "coffee": product.coffee, "milk": product.milk, "creammilk": product.creammilk, "chocolate_topping": product.chocolate_topping, "syrup": product.syrup, "chocolate": product.chocolate, "cocoa": product.cocoa, "icecream": product.icecream, "tea": product.tea, "cup_espresso": product.cup_espresso, "cup_small": product.cup_small, "cup_middle": product.cup_middle, "cup_big": product.cup_big}
    return jsonify(product_json)

@app.route('/api/product/<id>', methods=['DELETE'])
def api_product_delete(id):
    products = Product.query.filter_by(id=id)
    if not products:
        abort(404)
    product = products[0]
    db.session.delete(product)
    db.session.commit()
    return jsonify()

@app.route('/api/product/<id>', methods=['PUT'])
def api_product_update(id):
    updated_product = request.get_json()
    products_to_update = Product.query.filter_by(id=id)
    data = json.loads(request.get_data())
    product_to_update = products_to_update[0]
    product_to_update = db.session.query(Product).filter_by(id = id).first()
    product_to_update.name = data['name']
    product_to_update.type = data['type']
    product_to_update.size = data['size']
    product_to_update.price = data['price']
    product_to_update.coffee = data['coffee']
    product_to_update.milk = data['milk']
    product_to_update.creammilk = data['creammilk']
    product_to_update.chocolate_topping = data['chocolate_topping']
    product_to_update.syrup = data['syrup']
    product_to_update.chocolate = data['chocolate']
    product_to_update.cocoa = data['cocoa']
    product_to_update.icecream = data['icecream']
    product_to_update.tea = data['tea']
    product_to_update.cup_espresso = data['cup_espresso']
    product_to_update.cup_small = data['cup_small']
    product_to_update.cup_middle = data['cup_middle']
    product_to_update.cup_big = data['cup_big']
    db.session.commit()
    return jsonify(product_to_update.to_dict())

#api's for STOCK
@app.route('/api/stock', methods=['GET'])
def api_stock_get():
    stocks = Stock.query.all()
    stocks_json = [{"id": stock.id, "coffee": stock.coffee, "milk": stock.milk, "creammilk": stock.creammilk, "chocolate_topping": stock.chocolate_topping, "syrup": stock.syrup, "chocolate": stock.chocolate, "cocoa": stock.cocoa, "icecream": stock.icecream, "tea": stock.tea, "cup_espresso": stock.cup_espresso, "cup_small": stock.cup_small, "cup_middle": stock.cup_middle, "cup_big": stock.cup_big, "thermoglass1": stock.thermoglass1, 'wooden_icon1': stock.wooden_icon1, "wooden_icon2": stock.wooden_icon2, "coffee_250gr": stock.coffee_250gr, "postcard": stock.postcard, "chips_with_basil": stock.chips_with_basil, "chips_with_banana": stock.chips_with_banana, "chips_with_orange": stock.chips_with_orange, "chips_with_fruit_mix": stock.chips_with_fruit_mix, "chips_with_pinapple": stock.chips_with_pinapple, "chips_with_watermelon": stock.chips_with_watermelon, "chips_with_mango": stock.chips_with_mango, "chips_with_pear": stock.chips_with_pear, "chips_with_cocos": stock.chips_with_cocos, "chips_with_melon": stock.chips_with_melon, "sandwich_with_chicken": stock.sandwich_with_chicken, "protein_snack": stock.protein_snack, "muffin": stock.muffin, "donut": stock.donut, "cookie": stock.cookie, "fruit_snack": stock.fruit_snack, "macarons": stock. macarons, "wagon_wheels": stock.wagon_wheels, "nutella": stock.nutella, "mini_ritter_sport": stock.mini_ritter_sport}
                  for stock in stocks]
    return jsonify(stocks_json)

@app.route('/api/stock/<id>', methods=['GET'])
def api_stock_get_id(id):
    stocks = Stock.query.filter_by(id=id)
    if not stocks:
        abort(404)
    stock = stocks[0]
    stock_json = {"id": stock.id, "coffee": stock.coffee, "milk": stock.milk, "creammilk": stock.creammilk, "chocolate_topping": stock.chocolate_topping, "syrup": stock.syrup, "chocolate": stock.chocolate, "cocoa": stock.cocoa, "icecream": stock.icecream, "tea": stock.tea, "cup_espresso": stock.cup_espresso, "cup_small": stock.cup_small, "cup_middle": stock.cup_middle, "cup_big": stock.cup_big, "thermoglass1": stock.thermoglass1, 'wooden_icon1': stock.wooden_icon1, "wooden_icon2": stock.wooden_icon2, "coffee_250gr": stock.coffee_250gr, "postcard": stock.postcard, "chips_with_basil": stock.chips_with_basil, "chips_with_banana": stock.chips_with_banana, "chips_with_orange": stock.chips_with_orange, "chips_with_fruit_mix": stock.chips_with_fruit_mix, "chips_with_pinapple": stock.chips_with_pinapple, "chips_with_watermelon": stock.chips_with_watermelon, "chips_with_mango": stock.chips_with_mango, "chips_with_pear": stock.chips_with_pear, "chips_with_cocos": stock.chips_with_cocos, "chips_with_melon": stock.chips_with_melon, "sandwich_with_chicken": stock.sandwich_with_chicken, "protein_snack": stock.protein_snack, "muffin": stock.muffin, "donut": stock.donut, "cookie": stock.cookie, "fruit_snack": stock.fruit_snack, "macarons": stock. macarons, "wagon_wheels": stock.wagon_wheels, "nutella": stock.nutella, "mini_ritter_sport": stock.mini_ritter_sport}
    return jsonify(stock_json)

@app.route('/api/stock', methods=['POST'])
def api_stock_insert():
    new_stock = request.get_json()
    stock = Stock(id=new_stock['id'], name=new_stock['name'], type=new_stock['type'], size=new_stock['size'], price=new_stock['price'], coffee=new_stock['coffee'], milk=new_stock['milk'], creammilk=new_stock['creammilk'], chocolate_topping=new_stock['chocolate_topping'], syrup=new_stock['syrup'], chocolate=new_stock['chocolate'], cocoa=new_stock['cocoa'], icecream=new_stock['icecream'], tea=new_stock['tea'], cup_espresso=new_stock['cup_espresso'], cup_small=new_stock['cup_small'], cup_middle=new_stock['cup_middle'], cup_big=new_stock['cup_big'])
    db.session.add(stock)
    db.session.commit()
    stock_json = {"id": stock.id, "name": stock.name, "type": stock.type, "size": stock.size, "price": stock.price, "coffee": stock.coffee, "milk": stock.milk, "creammilk": stock.creammilk, "chocolate_topping": stock.chocolate_topping, "syrup": stock.syrup, "chocolate": stock.chocolate, "cocoa": stock.cocoa, "icecream": stock.icecream, "tea": stock.tea, "cup_espresso": stock.cup_espresso, "cup_small": stock.cup_small, "cup_middle": stock.cup_middle, "cup_big": stock.cup_big}
    return jsonify(stock_json)

@app.route('/api/stock/<id>', methods=['DELETE'])
def api_stock_delete(id):
    stocks = Stock.query.filter_by(id=id)
    if not stocks:
        abort(404)
    stock = stocks[0]
    db.session.delete(stock)
    db.session.commit()
    return jsonify()

@app.route('/api/stock/<id>', methods=['PUT'])
def api_stock_update(id):
    updated_stock = request.get_json()
    stocks_to_update = Stock.query.filter_by(id=id)
    data = json.loads(request.get_data())
    stock_to_update = stocks_to_update[0]
    stock_to_update = db.session.query(Stock).filter_by(id = id).first()
    stock_to_update.coffee = data['coffee']
    stock_to_update.milk = data['milk']
    stock_to_update.creammilk = data['creammilk']
    stock_to_update.chocolate_topping = data['chocolate_topping']
    stock_to_update.syrup = data['syrup']
    stock_to_update.chocolate = data['chocolate']
    stock_to_update.cocoa = data['cocoa']
    stock_to_update.icecream = data['icecream']
    stock_to_update.tea = data['tea']
    stock_to_update.cup_espresso = data['cup_espresso']
    stock_to_update.cup_small = data['cup_small']
    stock_to_update.cup_middle = data['cup_middle']
    stock_to_update.cup_big = data['cup_big']
    stock_to_update.thermoglass1 = data['thermoglass1']
    stock_to_update.wooden_icon1 = data['wooden_icon1']
    stock_to_update.wooden_icon2 = data['wooden_icon2']
    stock_to_update.coffee_250gr = data['coffee_250gr']
    stock_to_update.postcard = data['postcard']
    stock_to_update.chips_with_basil = data['chips_with_basil']
    stock_to_update.chips_with_banana = data['chips_with_banana']
    stock_to_update.chips_with_orange = data['chips_with_orange']
    stock_to_update.chips_with_fruit_mix = data['chips_with_fruit_mix']
    stock_to_update.chips_with_pinapple = data['chips_with_pinapple']
    stock_to_update.chips_with_watermelon = data['chips_with_watermelon']
    stock_to_update.chips_with_mango = data['chips_with_mango']
    stock_to_update.chips_with_pear = data['chips_with_pear']
    stock_to_update.chips_with_cocos = data['chips_with_cocos']
    stock_to_update.chips_with_melon = data['chips_with_melon']
    stock_to_update.sandwich_with_chicken = data['sandwich_with_chicken']
    stock_to_update.protein_snack = data['protein_snack']
    stock_to_update.muffin = data['muffin']
    stock_to_update.donut = data['donut']
    stock_to_update.cookie = data['cookie']
    stock_to_update.fruit_snack = data['fruit_snack']
    stock_to_update.macarons = data['macarons']
    stock_to_update.wagon_wheels = data['wagon_wheels']
    stock_to_update.nutella = data['nutella']
    stock_to_update.mini_ritter_sport = data['mini_ritter_sport']
    db.session.commit()
    return jsonify(stock_to_update.to_dict())