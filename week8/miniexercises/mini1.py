def calculate_price(base_price, tax_rate):
    total = base_price * (1 + tax_rate)
    return total

print(calculate_price(100, 0.2))
