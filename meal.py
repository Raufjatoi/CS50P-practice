def main():
    t = input('What time is it? ')
    time = float(convert(t))
    if 7.0 <= time < 8.0:
        print('Breakfast time')
    elif 12.0 <= time < 13.0:
        print('Lunch time')
    elif 18.0 <= time < 19.0:
        print('Dinner time')
    else:
        pass

def convert(time):
    h, t = time.split(':')
    return int(h) + float(t)/60

if __name__ == "__main__":
    main()
