from app import app
from models import Customer
from models import Owner
from models import Deal
from models import Car
from flask import jsonify
from flask import request
from app import db
import json

#api's for customer
@app.route('/api/customer', methods=['GET'])
def api_customer_get():
    customers = Customer.query.all()
    customers_json = [{"id": customer.id, "name": customer.name}
                  for customer in customers]
    return jsonify(customers_json)

@app.route('/api/customer/<id>', methods=['GET'])
def api_customer_get_id(id):
    customers = Customer.query.filter_by(id=id)
    if not customers:
        abort(404)
    customer = customers[0]
    customer_json = {"id": customer.id, "name": customer.name}
    return jsonify(customer_json)

@app.route('/api/customer', methods=['POST'])
def api_customer_insert():
    new_customer = request.get_json()
    customer = Customer(id=new_customer['id'], name=new_customer['name'])
    db.session.add(customer)
    db.session.commit()
    customer_json = {"id": customer.id, "name": customer.name}
    return jsonify(customer_json)

@app.route('/api/customer/<id>', methods=['DELETE'])
def api_customer_delete(id):
    customers = Customer.query.filter_by(id=id)
    if not customers:
        abort(404)
    customer = customers[0]
    db.session.delete(customer)
    db.session.commit()
    return jsonify()

@app.route('/api/customer/<id>', methods=['PUT'])
def api_customer_update(id):
    updated_customer = request.get_json()
    customers_to_update = Customer.query.filter_by(id=id)
    data = json.loads(request.get_data())
    customer_to_update = customers_to_update[0]
    customer_to_update = db.session.query(Customer).filter_by(id = id).first()
    customer_to_update.name = data['name']
    db.session.commit()
    return jsonify(customer_to_update.to_dict())

#api's for owner
@app.route('/api/owner', methods=['GET'])
def api_owner_get():
    owners = Owner.query.all()
    owners_json = [{"id": owner.id, "name": owner.name}
                  for owner in owners]
    return jsonify(owners_json)

@app.route('/api/owner/<id>', methods=['GET'])
def api_owner_get_id(id):
    owners = Owner.query.filter_by(id=id)
    if not owners:
        abort(404)
    owner = owners[0]
    owner_json = {"id": owner.id, "name": owner.name}
    return jsonify(owner_json)

@app.route('/api/owner', methods=['POST'])
def api_owner_insert():
    new_owner = request.get_json()
    owner = Owner(id=new_owner['id'], name=new_owner['name'])
    db.session.add(owner)
    db.session.commit()
    owner_json = {"id": owner.id, "name": owner.name}
    return jsonify(owner_json)

@app.route('/api/owner/<id>', methods=['DELETE'])
def api_owner_delete(id):
    owners = Owner.query.filter_by(id=id)
    if not owners:
        abort(404)
    owner = owners[0]
    db.session.delete(owner)
    db.session.commit()
    return jsonify()

@app.route('/api/owner/<id>', methods=['PUT'])
def api_owner_update(id):
    updated_owner = request.get_json()
    owners_to_update = Owner.query.filter_by(id=id)
    data = json.loads(request.get_data())
    owner_to_update = owners_to_update[0]
    owner_to_update = db.session.query(Owner).filter_by(id = id).first()
    owner_to_update.name = data['name']
    db.session.commit()
    return jsonify(owner_to_update.to_dict())

#api's for deal
@app.route('/api/deal', methods=['GET'])
def api_deal_get():
    deals = Deal.query.all()
    deals_json = [{"id": deal.id, "owner": deal.owner, "customer": deal.customer, "car": deal.car}
                  for deal in deals]
    return jsonify(deals_json)

@app.route('/api/deal/<id>', methods=['GET'])
def api_deal_get_id(id):
    deals = Deal.query.filter_by(id=id)
    if not deals:
        abort(404)
    deal = deals[0]
    deal_json = {"id": deal.id, "owner": deal.owner, "customer": deal.customer, "car": deal.car}
    return jsonify(deal_json)

@app.route('/api/deal', methods=['POST'])
def api_deal_insert():
    new_deal = request.get_json()
    deal = Deal(id=new_deal['id'], owner=new_deal['owner'], customer=new_deal['customer'], car=new_deal['car'])
    db.session.add(deal)
    db.session.commit()
    deal_json = {"id": deal.id, "owner": deal.owner, "customer": deal.customer, "car": deal.car}
    return jsonify(deal_json)

@app.route('/api/deal/<id>', methods=['DELETE'])
def api_deal_delete(id):
    deals = Deal.query.filter_by(id=id)
    if not deals:
        abort(404)
    deal = deals[0]
    db.session.delete(deal)
    db.session.commit()
    return jsonify()

@app.route('/api/deal/<id>', methods=['PUT'])
def api_deal_update(id):
    updated_deal = request.get_json()
    deals_to_update = Deal.query.filter_by(id=id)
    data = json.loads(request.get_data())
    deal_to_update = deals_to_update[0]
    deal_to_update = db.session.query(Deal).filter_by(id = id).first()
    deal_to_update.owner = data['owner']
    deal_to_update.customer = data['customer']
    deal_to_update.car = data['car']
    db.session.commit()
    return jsonify(deal_to_update.to_dict())

#api's for car
@app.route('/api/car', methods=['GET'])
def api_car_get():
    cars = Car.query.all()
    cars_json = [{"id": car.id, "name": car.name, "price": car.price, "year": car.year, "mileage": car.mileage}
                  for car in cars]
    return jsonify(cars_json)

@app.route('/api/car/<id>', methods=['GET'])
def api_car_get_id(id):
    cars = Car.query.filter_by(id=id)
    if not cars:
        abort(404)
    car = cars[0]
    car_json = {"id": car.id, "name": car.name, "price": car.price, "year": car.year, "mileage": car.mileage}
    return jsonify(car_json)

@app.route('/api/car', methods=['POST'])
def api_car_insert():
    new_car = request.get_json()
    car = Car(id=new_car['id'], name=new_car['name'], price=new_car['price'], year=new_car['year'], mileage=new_car['mileage'])
    db.session.add(car)
    db.session.commit()
    car_json = {"id": car.id, "name": car.name, "price": car.price, "year": car.year, "mileage": car.mileage}
    return jsonify(car_json)

@app.route('/api/car/<id>', methods=['DELETE'])
def api_car_delete(id):
    cars = Car.query.filter_by(id=id)
    if not cars:
        abort(404)
    car = cars[0]
    db.session.delete(car)
    db.session.commit()
    return jsonify()

@app.route('/api/car/<id>', methods=['PUT'])
def api_car_update(id):
    updated_car = request.get_json()
    cars_to_update = Car.query.filter_by(id=id)
    data = json.loads(request.get_data())
    car_to_update = cars_to_update[0]
    car_to_update = db.session.query(Car).filter_by(id = id).first()
    car_to_update.name = data['name']
    car_to_update.price = data['price']
    car_to_update.year = data['year']
    car_to_update.mileage = data['mileage']
    db.session.commit()
    return jsonify(car_to_update.to_dict())
