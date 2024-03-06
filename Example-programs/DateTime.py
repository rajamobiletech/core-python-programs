import datetime


currentDateTime = datetime.datetime(2024, 3, 2, 10, 40, 46)
print(currentDateTime)


currentTime = datetime.time(9, 40, 23, +530)
print(currentTime)


print(datetime.datetime.now())

print(datetime.datetime.weekday(datetime.datetime.now()))

print(datetime.date.today())

print(datetime.datetime.strptime('15/11/2000', '%d/%m/%Y'))

print("================")

date_string = "25 December, 2022"
print("date_string =", date_string)

# use strptime() to create date object
date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)

print("================")

# current date and time
now = datetime.datetime.now()

t = now.strftime("%H:%M:%S")
print("Time:", t)

print("______________________________________________________________")

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

s3 = now.strftime("%d %B %y, %I:%M:%S %p")
# dd/mm/YY H:M:S format
print("s3:", s3)

s4 = now.strftime("%c")
# dd/mm/YY H:M:S format
print("s4:", s4)

import pytz

local = datetime.datetime.now()
print("Local:", local.strftime("%B/%d/%Y, %H:%M:%S"))


tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

#calender :---
#first import calendar :-
import calendar

#assign a variable which "year" you want:- 
year=2024

#assign a variable "month"
month=3

#print the year and month
print(calendar.month(year,month))

#print whole year:-
year=2024
print(calendar.calendar(year))