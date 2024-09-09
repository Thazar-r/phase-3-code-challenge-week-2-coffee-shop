class Coffee:
    def __init__(self, type, price):
        self.type = type
        self.price = price

    def __str__(self):
        return f"{self.type} - ${self.price}"

