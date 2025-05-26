# import datetime as dt
import calendar
from datetime import *


today = date.today()
print(today)


Current_time = datetime.now()
print(f'current datetime {Current_time}')

formatted = Current_time.strftime("%d-%m-%y %H-%M-%S")
print(f'formated datetime: {formatted}')

date_str = '2025-05-25 12:02:01'
Dates= datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(f'date to string: {Dates}')

today = date.today()
future = today + timedelta(days=7)
print(f'7 Days from today:{future}')

#difference b/w two dates

d1 = date(2025, 1, 1)
d2 = date(2025, 5, 25)
delta = d2 - d1
print(f'Days b/w : {delta.days}')

#leap Year

def is_leapYear(year):
    return (year % 4 == 0 and year % 100!= 0) or (year % 400 == 0)

print(is_leapYear(2024))

#weekday of a given date

date_obj = datetime.strptime("2025-05-25", "%Y-%m-%d")
print(f'Weekday: {date_obj.strftime("%A")}')

#find first day of month

def first_day_of_month():
    today = date.today()
    return date(today.year, today.month, 1)

print("First day of the month: ",first_day_of_month().strftime("%A"))

#Generate list of dates

today = date.today()
date = [today + timedelta(days = i) for i in range(7)]

for d in date:
    print(d)
    
#get all modays in a given month


from datetime import date
def get_mondays(year, month):
    mondays = []
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        if week[calendar.MONDAY] != 0:
            mondays.append(date(year, month, week[calendar.MONDAY]))
    return mondays


monday = get_mondays(2025, 5)

for mon in monday:
    print(mon)


#check if given date is a weekend

def is_weekend(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.weekday() >=5

print(is_weekend("2025-5-25"))

#print text calender for current month

now = datetime.now()
print(calendar.month(now.year, now.month))

#days left until next birthday

def days_until(birth_month, birthdate):
    today = date.today()
    current_year_birthday = date(today.year, birth_month, birthdate)
    
    if current_year_birthday < today:
        next_birthday = date(today.year + 1, birth_month, birthdate)
    else: 
        next_birthday = current_year_birthday
    return(next_birthday - today).days

print(days_until(11,8))

import datetime
import calendar

# Get today's date
today = datetime.date.today()

# Get the last day of the current month
last_day = calendar.monthrange(today.year, today.month)[1]
last_date = datetime.date(today.year, today.month, last_day)

print("Last day of the month:", last_date.strftime("%A"))

print(today.strftime("%A"))
