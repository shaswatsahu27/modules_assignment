# billing.py

def calculate_total(prices):
    return sum(prices)

def apply_tax(price, tax_percent):
    return price + (price * tax_percent / 100)
