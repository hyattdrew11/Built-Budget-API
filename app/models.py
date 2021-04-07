from datetime import datetime
from app import db, ma

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class BudgetItem(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(140))
    customer_id     = db.Column(db.Integer, db.ForeignKey("customer.id"))
    customer        = db.relationship("Customer", backref="BudgetItems")
    amount          = db.Column(db.Integer, default=0, nullable=False)
    date_created    = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)
    date_modified   = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)

    # def __repr__(self):
    #     return '<BudgetItem {}>'.format(self.id)

class CustomerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Customer

    id      = ma.auto_field()
    name    = ma.auto_field()

class BudgetItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = BudgetItem

    id      = ma.auto_field()
    name    = ma.auto_field()