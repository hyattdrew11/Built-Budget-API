#!
'''
..%%%%...%%%%%%..%%%%%%..........%%%%%...%%..%%..%%%%%%..%%......%%%%%%.
.%%......%%........%%............%%..%%..%%..%%....%%....%%........%%...
.%%.%%%..%%%%......%%............%%%%%...%%..%%....%%....%%........%%...
.%%..%%..%%........%%............%%..%%..%%..%%....%%....%%........%%...
..%%%%...%%%%%%....%%............%%%%%....%%%%...%%%%%%..%%%%%%....%%...
........................................................................
'''
from flask import render_template, flash, redirect, url_for, jsonify, request, abort
from app import app, db
from app.models import Customer, BudgetItem, CustomerSchema, BudgetItemSchema
from marshmallow import validate, ValidationError
import json
from boto import kinesis
from flask_cors import CORS

CORS(app)

customer_schema = CustomerSchema()
budget_schema = BudgetItemSchema(many=True)
kinesis = kinesis.connect_to_region(app.config['AWS_REGION'])
# kinesis.describe_stream(app.config['KINESIS_DATA_STREAM'])

@app.route('/')
@app.route('/index')
def index():
    customers   = Customer.query.all()
    return render_template('index.html', title='Get Built', customers=customers)

@app.route('/customers')
def get_customers():
    # STARTING TO BUILD OUT VUE FRONT END CONNECTION
    customers   = Customer.query.all()
    many_customers = CustomerSchema(many=True)
    res = many_customers.dumps(customers)
    return res, 202

# ADD A NEW CUSTOMER
@app.route("/customer/details", methods=['POST',])
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
            new_customer = Customer(**data)
            db.session.add(new_customer)
            db.session.commit()
            try:
                nc = customer_schema.dump(new_customer)
                kinesis.put_record(app.config['KINESIS_DATA_STREAM'], json.dumps(nc), "partitionkey")
            except Exception as e:
                print(e)
                # CALL TO CLOUD WATCH OR OTHER ALERTING SYSTEM

            response = { 'message': 'new customer registered', 'data': customer_schema.dump(new_customer) }
            return jsonify(response), 202
    except ValidationError as err:
            errors = err.messages
            validate = False
            return jsonify(errors), 403

# GET CUSTOMER DETAILS
@app.route("/customer/details/<customer_id>", methods=['GET', 'DELETE'])
def get_customer(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()
    if customer is None:
        response = { 'message': 'customer does not exist' }
        return jsonify(response), 404
    else:
        if request.method == 'GET':
            result = customer_schema.dump(customer)
            response= { 'data': result }
            return jsonify(response), 202
        elif request.method == 'DELETE':
            db.session.delete(customer)
            db.session.commit()
            response = { 'message': 'customer' + customer_id + ' deleted' }
            return jsonify(response), 202
        else:
            return jsonify(response), 404

# GET ALL BUDGET ITEMS FOR A CUSTOMER
@app.route("/budget/details/<customer_id>", methods=['GET'])
def get_budget_items(customer_id):
    items = BudgetItem.query.filter_by(customer_id=customer_id).all()
    if items is None:
        response = { 'message': 'customer does not exist' }
        return jsonify(response), 404
    else:
        result = budget_schema.dump(items)
        response = {'data': result, 'status_code' : 202 }
        return jsonify(response)

# ADD OR UPDATE A NEW BUDGET ITEM
@app.route("/budget/details", methods=['POST', 'PUT'])
def create_budget_item():
    data = request.get_json()
    print(data)
    print("Update a budget item")
    try:
         # VALIDATE JSON DATA
         # AS WE HAVE ONE TO MANY RELATIONSHIP FROM CUSTOMER TO BUDGET ITEM DATA MUST BE ARRAY NOT OBJECT
        validate = budget_schema.loads(json.dumps(data))
    except ValidationError as err:
        errors = err.messages
        return jsonify(errors), 403
    if request.method == 'POST':
         # THERE IS A MORE ELEGANT WAY TO DO THIS, BUT WANT THE ABILITY TO ADD MANY BUDGET ITEMS AT ONCE
        items = []
        for x in data:
            new_item = BudgetItem(**x)
            db.session.add(new_item)
            db.session.commit()
            items.append(new_item)

        items = budget_schema.dump(items)
        response = { 'message': 'new budget item created','data': items }

        return response, 202
    elif request.method == 'PUT':
        print("PUT")
        # THERE IS A MORE ELEGANT WAY TO DO THIS, BUT WANT THE ABILITY TO ADD MANY BUDGET ITEMS AT ONCE
        items = []
        for x in data:
            item = BudgetItem.query.filter_by(id=x['id']).update(dict(**x))
            db.session.commit()
            items.append(x)

        items = budget_schema.dump(items)
        response = { 'message': 'new budget item created', 'data' : items }
        return jsonify(response), 202
    else:
        print("ELSE")
        return abort(400)

# DELETE A BUDGET ITEM
@app.route("/budget/details/<item_id>", methods=['DELETE'])
def delete_budget_item(item_id):
    item = BudgetItem.query.filter_by(id=item_id).first()
    if item is None:
        response = { 'message': 'budget item does not exist' }
        return jsonify(response), 404
    else:
        db.session.delete(item)
        db.session.commit()
        response = { 'message': 'budget item ' + item_id + ' deleted' }
        return jsonify(response), 202
'''
..%%%%...%%%%%%..%%%%%%..........%%%%%...%%..%%..%%%%%%..%%......%%%%%%.
.%%......%%........%%............%%..%%..%%..%%....%%....%%........%%...
.%%.%%%..%%%%......%%............%%%%%...%%..%%....%%....%%........%%...
.%%..%%..%%........%%............%%..%%..%%..%%....%%....%%........%%...
..%%%%...%%%%%%....%%............%%%%%....%%%%...%%%%%%..%%%%%%....%%...
........................................................................
'''