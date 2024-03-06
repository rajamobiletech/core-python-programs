#ifrst import date and time:-
import datetime

#it print what you type here that prints as output:-
print(datetime.datetime(2024,3,4,10,24,30))

#it prints present date and time:- 
print(datetime.datetime.now())

#it is also shows present date and time:-
print(datetime.datetime.today())

#
print(datetime.datetime.weekday(datetime.datetime.now()))

#it is print first year/month/day:-
print(datetime.datetime.strptime('14/04/2003', '%d/%m/%Y'))

#it prints the present date and also present time:-
a=datetime.datetime.now()
b=a.strftime("%H:%M:%S")
print("time",b)
print("_________________________________________________________________")

import datetime
presentdatetime=datetime.datetime(2024, 3, 5,)
print(presentdatetime)

presenttime=datetime.time(3 , 17 , 20, +145)
print(presenttime)


 

print(datetime.datetime.weekday(datetime.datetime.today()))

print(datetime.datetime.strptime('5/3/2024','%d/%m/%Y'))

date="05 feb, 2024"
print("date = ",date)


dateobject=datetime.datetime.strptime(date,"%d, %B, %Y")
print(dateobject)



import datetime
print(datetime.datetime.today())

print(datetime.date.today())

print(datetime.datetime.strptime('14/4/2003', '%M/%d/%Y'))

a=(datetime.datetime.now())
print(a)

print(datetime.datetime.weekday(datetime.datetime.now()))

b=a.strftime("%c")
print(b)

c=a.strftime("%a")
print(c)
d=a.strftime("%b")
print(d)

e=a.strftime("%c")
print(e)

e1=a.strftime("%d")
print(e1)

e2=a.strftime("%e")
print(e2)

e3=a.strftime("%f")
print(e3)

e4=a.strftime("%g")
print(e4)


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