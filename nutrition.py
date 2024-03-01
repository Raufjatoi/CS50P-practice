fc = {
    "apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "pear": 100,
    "Sweet Cherries":100
}
i = input('Item: ')
if i in fc:
    print(f'Calories: {fc[i]}')
