#6/7
from collections import defaultdict

d = defaultdict(int)

while True:
    try:
        item = input("").upper()
        d[item] += 1
    except EOFError:
        break

for key, value in d.items():
    print(f"{value} {key}")


                     #Chatgpt