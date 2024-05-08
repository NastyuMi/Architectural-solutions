# output_1.py

class Address:
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def is_new_york(self):
        return self.state == "New York"

    def is_california(self):
        return self.state == "California"

    def format_address(self):
        return f"{self.street}, {self.city}, {self.state} {self.zipcode}"

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class ShippingStrategy:
    def calculate_shipping_cost(self, address):
        raise NotImplementedError

class StandardShippingStrategy(ShippingStrategy):
    def calculate_shipping_cost(self, address):
        if address.is_new_york():
            return 5.00
        elif address.is_california():
            return 10.00
        else:
            return 15.00

class Order:
    def __init__(self, customer, product, quantity, shipping_strategy):
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.shipping_strategy = shipping_strategy

    def print_order_details(self):
        print(f"Order for {self.product} x {self.quantity}")
        print(f"Shipping to {self.customer.address.format_address()}")

    def calculate_shipping_cost(self):
        return self.shipping_strategy.calculate_shipping_cost(self.customer.address)