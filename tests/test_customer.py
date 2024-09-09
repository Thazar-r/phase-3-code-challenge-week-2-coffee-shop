import pytest
from customer import Customer

def test_customer_creation():
    customer = Customer("Quincy Jones", "quincy@example.com")
    assert customer.name == "Quincy Jones"
    assert customer.email == "quincy@example.com"
    assert str(customer) == "Quincy Jones (quincy@example.com)"