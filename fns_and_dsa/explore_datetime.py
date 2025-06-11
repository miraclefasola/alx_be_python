import datetime


def display_current_datetime():
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)
display_current_datetime()

days = int(input("Enter the number of days to add to the current date: "))

from datetime import timedelta


def calculate_future_date():
    future_date = datetime.datetime.now() + timedelta(days)
    print(future_date.strftime("%Y-%m-%d %H:%M:%S"))

calculate_future_date()





