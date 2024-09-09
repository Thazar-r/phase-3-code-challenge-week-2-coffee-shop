import pytest
from coffee import Coffee

def test_coffee_creation():
    coffee = Coffee("Latte", 3.5)
    assert coffee.type == "Latte"
    assert coffee.price == 3.5
    assert str(coffee) == "Latte - $3.5"