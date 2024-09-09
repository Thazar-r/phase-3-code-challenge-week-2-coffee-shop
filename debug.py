# Import the necessary classes
from customer import Customer
from coffee import Coffee
from order import Order

# Create some sample data
customer1 = Customer("Alice", "alice@example.com")
coffee1 = Coffee("Latte", 3.50)

# Place an order
order1 = customer1.place_order(coffee1)

# Debug output to verify the relationships
print(f"Customer: {customer1.name}, Email: {customer1.email}")
print(f"Ordered Coffee: {coffee1.name}, Price: ${coffee1.price}")
print(f"Total Orders by {customer1.name}: {len(customer1.orders)}")
print(f"Total Orders for {coffee1.name}: {len(coffee1.orders)}")