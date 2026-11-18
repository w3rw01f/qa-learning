accounts = {
    "40817": {"balance": 1500.0, "currency": "USD"},
    "40702": {"balance": 320.5, "currency": "EUR"},
    "42301": {"balance": 0, "currency": "GEL"}
}

# task 1
print(type(1500))
print(type("1500"))
print(type(1500.0))
print(type(True))

# task 2
print(float("250.75")+100)

# task 3
transactions = [125.50, 47.99, -230.00, 1008.75, -89.25]
print(sum(transactions))
print(max(transactions))

# task 4
neg_transactions = []
for transaction in transactions:
    if transaction < 0:
        neg_transactions.append(transaction)
print(neg_transactions)

# task 5
big_count = 0
for transaction in transactions:
    if transaction > 1000:
        big_count += 1
print(big_count)

# task 6
usd_rates = {
    "EUR": 0.893416,
    "RUB": 82.5486
}

print(round(100/usd_rates["EUR"], 2))

# task 7
usd_rates["GEL"] = 2.5936
del usd_rates["RUB"]
print(usd_rates)

# task 8
for account, details in accounts.items():
    print(account, details["balance"])

# task 9
currencies = set()

for details in accounts.values():
    currencies.add(details["currency"])

print(currencies)

# task 10
def is_valid_true(value):
    return len(str(value)) == 5 and str(value).isdigit()

print(is_valid_true("1234a"))  # False
print(is_valid_true(1234))     # False

# task 11
def apply_fee(amount, percent):
    return round(amount - amount * percent/100, 2)

print (apply_fee(100, 5))