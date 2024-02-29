## 29 Leap day idk wha it is hehe 2024
expression = input('Expression : ')
x, y, z = expression.split(" ")
if y == '+':
    print(float(int(x) + int(z)))
elif y == '-':
    print(float(x) - int(z))
elif y == '/':
    print(float(x) / int(z))
elif y == '*':
    print(float(x) * int(z))
else:
    print(expression)