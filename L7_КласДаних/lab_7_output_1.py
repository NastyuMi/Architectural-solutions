# output_1.py

class Product:
    def __init__(self, product_id, name, category, price):
        self.__product_id = product_id  # Приватне поле
        self.__name = name  # Приватне поле
        self.__category = category  # Приватне поле
        self.__price = price  # Приватне поле

    # Геттери для доступу до приватних полів
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    # Сеттери для встановлення значень приватних полів (необов'язково)
    def set_name(self, name):
        self.__name = name

    def set_category(self, category):
        self.__category = category

    def set_price(self, price):
        self.__price = price

class InventoryManagement:
    def __init__(self, products):
        self.products = products

    def print_product_details(self, product_id):
        for product in self.products:
            if product.get_product_id() == product_id:
                print(
                    f"Product ID: {product.get_product_id()}, "
                    f"Name: {product.get_name()}, "
                    f"Category: {product.get_category()}, "
                    f"Price: {product.get_price()}"
                )

