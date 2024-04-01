# pip install python-dateutil

from datetime import datetime
import re
import calendar
from dateutil import parser


def get_date():
    input_date = input("Enter the date: day, month, year: ")
    return input_date


def is_valid_date(input_date):
    try:
        parser.parse(input_date)
        return True
    except ValueError:
        return False


def check_date(input_date):
    date_parts = re.split(r"[\s,-.,_]", input_date)
    day = date_parts[0]
    month = date_parts[1]
    year = date_parts[2]
    try:
        if day.isdigit() and year.isdigit():
            day = int(day)
            year = int(year)
        else:
            raise ValueError("Day and Year must be integers")

        if month.isdigit():
            month = int(month)
        elif month.isalpha():
            month = month.capitalize()
        else:
            raise ValueError("Month must be an integer or a string")
    except ValueError as e:
        print(e)
        return None
    return (day, month, year)


def get_index_month(month_name):
    month = month_name.capitalize()
    month_to_index = {
        month: index for index, month in enumerate(calendar.month_name[1:], start=1)
    }
    month = month_to_index.get(month)
    return month


def format_date(day, month, year):
    if isinstance(month, str):
        month = get_index_month(month)

    date = f"{day} {month} {year}"
    return date


def transform_date(date):
    date_iso = datetime.strptime(date, "%d %m %Y").isoformat()
    date_norwegian = datetime.strptime(date, "%d %m %Y").strftime("%d.%B.%Y")
    return (date_iso, date_norwegian)


def get_data_for_print(date_iso):
    date_obj = datetime.fromisoformat(date_iso)
    day = date_obj.strftime("%-d")
    month = date_obj.strftime("%B")
    year = date_obj.strftime("%Y")
    formatted_date = f"{day}.{month.lower()} {year}"

    week_num = date_obj.isocalendar()[1]
    day_of_week = date_obj.strftime("%A")
    current_date = datetime.now().date()
    
    if date_obj.date() < current_date:
        massage = f"{formatted_date} was a {day_of_week} in week {week_num}"
    elif date_obj.date() == current_date:
        massage = f"{formatted_date} is a {day_of_week} in week {week_num}"
    else:
        massage = f"{formatted_date} will be a {day_of_week} in week {week_num}"

    return massage


def main():
    date = get_date()
    if is_valid_date(date):
        date = format_date(*check_date(date))
        date_iso, date_norwegian = transform_date(date)

        print(f"Date in ISO format: {date_iso}")
        print(f"Date in Norwegian format: {date_norwegian}")
        print(get_data_for_print(date_iso))
    else:
        print("This is not a date.")


if __name__ == "__main__":
    main()


# I need advice on architecture,this is bad code :-)

# I have a double code in the functions - "month = month_name.capitalize()" 
