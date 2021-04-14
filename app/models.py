from datetime import datetime
from app import db, ma
from marshmallow import Schema, fields, validate
import random

SEED = False

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))


class BudgetItem(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(140))
    customer_id     = db.Column(db.Integer, db.ForeignKey("customer.id"))
    customer        = db.relationship("Customer", backref="budgetItems")
    amount          = db.Column(db.Float)
    date_created    = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)
    date_modified   = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)


class CustomerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Customer

    id              = ma.auto_field()
    name            = ma.auto_field()
    email           = fields.Email()
    budgetItems     = ma.auto_field()

class BudgetItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = BudgetItem
        include_fk = True

    id              = ma.auto_field()
    name            = ma.auto_field()
    customer_id     = ma.auto_field()
    amount          = fields.Float()

if SEED:
    customer_schema = CustomerSchema()
    budget_schema   = BudgetItemSchema()
    customers       = ['Cicayda', 'ATT', 'Verizon', 'Data Intel Group']
    item_types      = ['Foundation Repar', 'Corrugated Steel', 'MDL Board', 'Backup Generator']
    for i,c in enumerate(customers):
        customer = Customer(name=c)
        db.session.add(customer)

        for e, item in enumerate(item_types):
            budget_item = BudgetItem(name=item_types[random.randint(0, 3)],customer=customer, amount=random.randint(0, 6000))
            db.session.add(budget_item)

        db.session.commit()