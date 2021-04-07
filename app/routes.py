from flask import render_template, flash, redirect, url_for, jsonify, request
from app import app, db
from app.models import Customer, BudgetItem, CustomerSchema, BudgetItemSchema

from pprint import pprint
customer_schema = CustomerSchema()
budget_schema = BudgetItemSchema(many=True)


@app.route('/')
@app.route('/index')
def index():
    customers   = Customer.query.all()
    print(customers)
    parsed = jsonify(customer_schema.dump(customers))
    print(parsed)
    # budgetItems = BudgetItem.query.all()
    return render_template('index.html', title='Get Built', customers=customers, parsed=parsed)



@app.route("/customer/details", methods=['POST'])
def create_customer():
    data = request.get_json()
    print("POST REQUEST")
    print(data)
    if data['customer_name']:
        customer_name = data['customer_name']
        existing_customer=Customer.query.filter_by(name=customer_name).first()
        if existing_customer is not None:
            response = {
                  'message': 'customer already exists'
                    }
            return jsonify(response), 403

        new_customer = Customer(name=data['customer_name'])
        db.session.add(new_customer)
        db.session.commit()
        response = {
               'message': 'new customer registered'
                   }
        return jsonify(response), 202
    else:
        response = {
             'status': 'error',
             'message': 'bad request body'
                   }
        return jsonify(response), 400

@app.route("/customer/details/<customer_id>", methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()
    if customer is None:
        response = {
                 'message': 'customer does not exist'
                   }
        return jsonify(response), 404
    result = customer_schema.dump(customer)
    response= { 
        'data': result, 
        'status_code' : 202 
    }
    return jsonify(response)


@app.route("/budget/details/<customer_id>", methods=['GET'])
def get_budget_items(customer_id):
    items = BudgetItem.query.filter_by(customer_id=customer_id).all()
    if items is None:
        response = {
                 'message': 'customer does not exist'
                   }
        return jsonify(response), 404
    result = budget_schema.dump(items)
    print(result)
    response= { 
        'data': result, 
        'status_code' : 202 
    }
    return jsonify(response)

