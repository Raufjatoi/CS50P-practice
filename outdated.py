#10/12
from datetime import datetime

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def validate_date(date):
    for format_string in ['%m/%d/%Y', '%B %d, %Y', '%B %d %Y']:
        try:
            datetime.strptime(date, format_string)
            return True
        except ValueError:
            continue
    return False

def convert_to_iso(date):
    try:
        parsed_date = datetime.strptime(date, '%m/%d/%Y')
        return parsed_date.strftime('%Y-%m-%d')
    except ValueError:
        try:
            parsed_date = datetime.strptime(date, '%B %d, %Y')
            return parsed_date.strftime('%Y-%m-%d')
        except ValueError:
            parsed_date = datetime.strptime(date, '%B %d %Y')
            return parsed_date.strftime('%Y-%m-%d')

def main():
    while True:
        user_input = input("Date: ")
        if validate_date(user_input):
            iso_date = convert_to_iso(user_input)
            print(iso_date)
            break
        else:
            pass
if __name__ == "__main__":
    main()
