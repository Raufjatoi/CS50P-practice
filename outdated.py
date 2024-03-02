months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def get_date():
    while True:
        try:
            date_input = input("Enter a date in month-day-year format (e.g., 9/8/1636 or September 8, 1636): ")
            if '/' in date_input:
                month, day, year = date_input.split('/')
            else:
                month, day, year = date_input.split(' ')
                month = month.capitalize()
            month_index = months.index(month) + 1
            print(f"{year}-{month_index:02d}-{day:02d}")
            break
        except (ValueError, IndexError):
            print("Invalid date format. Please try again.")

if __name__ == "__main__":
    get_date()
