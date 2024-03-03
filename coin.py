import random
coin = random.choice(['Heads','Tales'])
cc = input('Enter f to Flip the coin : ').lower()
if cc in ['f','flip','yes','ye','yep','ff']:
    print(coin)
else:
    pass