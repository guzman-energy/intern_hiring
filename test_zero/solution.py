# Assume the first day of any year is a Monday, find if it's a Sunday

date = 333
date = date % 7
# 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday, 5 = Saturday, 6 = Sunday
if date == 6:
    print("It's a Sunday")

# write code to see if it's a Sunday 

import datetime

def is_sunday(date):
    # Check if the date is a Sunday
    return date.weekday() == 6

def main():
    # Example date
    date = datetime.datetime(2025, 5, 11)  # This is a Sunday

    if is_sunday(date):
        print(f"{date.strftime('%Y-%m-%d')} is a Sunday.")
    else:
        print(f"{date.strftime('%Y-%m-%d')} is not a Sunday.")

if __name__ == "__main__":
    main()