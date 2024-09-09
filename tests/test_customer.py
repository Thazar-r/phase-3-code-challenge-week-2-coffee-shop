import pytest
from customer import Customer

def test_customer_creation():
    customer = Customer("John Doe", "john@example.com")
    assert customer.name == "John Doe"
    assert customer.email == "john@example.com"
    assert str(customer) == "John Doe (john@example.com)"