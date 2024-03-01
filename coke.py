due_amount = 50
print(f'Amount Due: {due_amount}')

while due_amount > 0:
    user = int(input('Insert Coin: '))
    if user <= due_amount:
        due_amount -= user
        print(f'Amount Due: {due_amount}')
    else:
        change = user - due_amount
        if change == 0:  
            print(f'Change Owned: {change}')
        break


