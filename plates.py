import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    pattern = re.compile(r'^[A-Za-z]{2,4}\d+$')
    return bool(pattern.match(s))

main()
