c = input('camelcase: ')
snake_case = ''
for char in c:
    if char.isupper():
        snake_case += '_' + char.lower()
    else:
        snake_case += char
print(f'snake_case: {snake_case.lstrip("_")}')
