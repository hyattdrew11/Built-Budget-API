#!
'''
..%%%%...%%%%%%..%%%%%%..........%%%%%...%%..%%..%%%%%%..%%......%%%%%%.
.%%......%%........%%............%%..%%..%%..%%....%%....%%........%%...
.%%.%%%..%%%%......%%............%%%%%...%%..%%....%%....%%........%%...
.%%..%%..%%........%%............%%..%%..%%..%%....%%....%%........%%...
..%%%%...%%%%%%....%%............%%%%%....%%%%...%%%%%%..%%%%%%....%%...
........................................................................
'''
from flask import render_template, flash, redirect, url_for, jsonify, request
from app import app, db
from app.models import Customer, BudgetItem, CustomerSchema, BudgetItemSchema
from marshmallow import validate, ValidationError

customer_schema = CustomerSchema()
budget_schema = BudgetItemSchema(many=True)


@app.route('/')
@app.route('/index')
def index():
    customers   = Customer.query.all()
    parsed = jsonify(customer_schema.dump(customers))
    return render_template('index.html', title='Get Built', customers=customers, parsed=parsed)


# ADD A NEW CUSTOMER
@app.route("/customer/details", methods=['POST'])
def create_customer():
    data = request.get_json()
    # VALIDATE POST DATA
    try:
        validate = customer_schema.load(data)
        existing_customer = Customer.query.filter_by(name=data['name']).first()
        if existing_customer is not None:
            response = { 'message': 'customer already exists' }
            return jsonify(response), 403
        else:
            # VALIDATION COMPLETE ADD NEW CUSTOMER
            new_customer = Customer(name=data['name'], email=data['email'])
            db.session.add(new_customer)
            db.session.commit()
            response = { 'message': 'new customer registered' }
            return jsonify(response), 202
    except ValidationError as err:
            errors = err.messages
            validate = False
            return jsonify(errors), 403

# GET CUSTOMER DETAILS
@app.route("/customer/details/<customer_id>", methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()
    if customer is None:
        response = { 'message': 'customer does not exist' }
        return jsonify(response), 404
    else:
        result = customer_schema.dump(customer)
        response= { 
            'data': result, 
            'status_code' : 202 
        }
        return jsonify(response)

# ADD A NEW BUDGET ITEM
@app.route("/BUDGET/details", methods=['POST'])
def create_customer():
    data = request.get_json()
    # VALIDATE POST DATA
    try:
        validate = customer_schema.load(data)
        existing_customer = Customer.query.filter_by(name=data['name']).first()
        if existing_customer is not None:
            response = { 'message': 'customer already exists' }
            return jsonify(response), 403
        else:
            # VALIDATION COMPLETE ADD NEW CUSTOMER
            new_customer = Customer(name=data['name'], email=data['email'])
            db.session.add(new_customer)
            db.session.commit()
            response = { 'message': 'new customer registered' }
            return jsonify(response), 202
    except ValidationError as err:
            errors = err.messages
            validate = False
            return jsonify(errors), 403

# GET BUDGET ITEMS FOR CUSTOMER
@app.route("/budget/details/<customer_id>", methods=['GET'])
def get_budget_items(customer_id):
    items = BudgetItem.query.filter_by(customer_id=customer_id).all()
    if items is None:
        response = { 'message': 'customer does not exist' }
        return jsonify(response), 404
    else:
        result = budget_schema.dump(items)
        response= { 
            'data': result, 
            'status_code' : 202 
        }
        return jsonify(response)
        
'''
..%%%%...%%%%%%..%%%%%%..........%%%%%...%%..%%..%%%%%%..%%......%%%%%%.
.%%......%%........%%............%%..%%..%%..%%....%%....%%........%%...
.%%.%%%..%%%%......%%............%%%%%...%%..%%....%%....%%........%%...
.%%..%%..%%........%%............%%..%%..%%..%%....%%....%%........%%...
..%%%%...%%%%%%....%%............%%%%%....%%%%...%%%%%%..%%%%%%....%%...
........................................................................
'''