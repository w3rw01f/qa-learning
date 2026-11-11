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

print(100/usd_rates["EUR"])

# task 7
usd_rates["GEL"] = 2.5936
del usd_rates["RUB"]
print(usd_rates)
