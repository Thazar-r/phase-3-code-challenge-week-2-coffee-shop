class Order:
    def __init__(self, customer, coffee):
        self.customer = customer
        self.coffee = coffee

    def __str__(self):
        return f"Order: {self.customer} ordered {self.coffee}"