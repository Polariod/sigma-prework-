from datetime import date
import datetime


def main(dob):
    try:
        born = datetime.datetime.strptime(dob, "%d-%m-%Y")
    except ValueError:
        raise ValueError("Incorrect data format, should be dd-dd-YYYY.")
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


print(main("01-01-1990"))
