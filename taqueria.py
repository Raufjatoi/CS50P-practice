# 4/7
f = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_cost = 0.0  

while True:
    try:
        item = input('Item: ')
        if item.title() in f:
            total_cost += f[item]
            print(f'Total: ${total_cost:.2f}')
    except EOFError:
        break
