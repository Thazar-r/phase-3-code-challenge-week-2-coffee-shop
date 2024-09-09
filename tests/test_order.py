import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_creation():
    customer = Customer("Quincy Jones", "quincy@example.com")
    coffee = Coffee("Latte", 3.5)
    order = Order(customer, coffee)
    assert order.customer == customer
    assert order.coffee == coffee
    assert str(order) == "Order: Quincy Jones (quincy@example.com) ordered Latte - $3.5"