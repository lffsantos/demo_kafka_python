import json
from decimal import Decimal


class Order(object):
    order_id: str
    amount: Decimal
    email: str

    def __init__(self, order_id: str, amount: Decimal, email: str):
        self.order_id = order_id
        self.amount = amount
        self.email = email

    def __str__(self):
        return f'order_id={self.order_id}, amount={self.amount}, email={self.email}'

    def serialize(self):
        return {
            'order_id': self.order_id,
            'amount': str(self.amount),
            'email': self.email
        }
