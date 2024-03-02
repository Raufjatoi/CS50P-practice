# 10/14
while True:
    try:
        f = input('Fraction: ')
        x, y = map(int, f.split('/'))

        if y == 0:
            continue
        elif x > y:
            continue

        percentage = round((x / y) * 100)

        if percentage <= 1:
            print('E')
            break
        elif percentage >= 99:
            print('F')
            break
        else:
            print(f'{percentage}%')
            break

    except (ValueError, ZeroDivisionError):
        break