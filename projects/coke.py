amount_due = 50
amount_paid = 0

while amount_paid < 50:
    print(f"Amount Due: {amount_due}")
    insert_coin = int(input("Insert Coin: "))

    if insert_coin == 5:
        amount_due -= 5
        amount_paid += 5

    elif insert_coin == 10:
        amount_due -= 10
        amount_paid += 10

    elif insert_coin == 25:
        amount_due -= 25
        amount_paid += 25

    else:
        continue

change_owed = amount_paid - 50
print(f"Change Owed: {change_owed}")



