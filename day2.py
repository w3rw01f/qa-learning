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
a = 0
for transaction in transactions:
    if transaction > 1000:
        a += 1
print(a)

# task 6
