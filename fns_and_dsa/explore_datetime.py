import datetime


def display_current_datetime():
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)
display_current_datetime()

days = int(input("please enter a number of days: "))

from datetime import timedelta


def calculate_future_date():
    future_date = datetime.datetime.now().date() + timedelta(days)
    print(future_date)

calculate_future_date()





