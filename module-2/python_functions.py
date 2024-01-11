
def calculate_tax (bill, tax_rate):
    return round((tax_rate * bill) / 100)

print(calculate_tax(175.00, 15))