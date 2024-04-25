def _calculate_total_price(product_prices, discount):
    total_price = 0
    for price in product_prices:
        if discount:
            total_price += price * (1 - discount)  # Застосовуємо знижку
        else:
            total_price += price
    return total_price

def calculate_total_price(product_prices, discount=0.1):
    total_price = _calculate_total_price(product_prices, discount)
    return total_price

def calculate_total_price_with_tax(product_prices, discount=0.1, tax_rate=0.18):
    total_price = _calculate_total_price(product_prices, discount)
    total_price *= (1 + tax_rate)  # Додаємо податок
    return total_price
