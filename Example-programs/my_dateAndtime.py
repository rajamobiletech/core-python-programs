 #first import datetime:-
import datetime

#it prints present and datetime:-
print(datetime.datetime.now())

#it print only today date:-
print(datetime.date.today())
#
print(datetime.datetime.strptime('8/3/2024','%d/%m/%Y'))

now = datetime.datetime.now()
print(now)

#it prints first hours,minutes,sec(use of 'strftime' We can change it as we like
#frost hours or first minutes like this %M:%S:%H or %S:%M:%H):-
now1=now.strftime("%H:%M:%S")
print(now1)
now2=now.strftime("%d/%m/%Y,%H:%M:%S")
print(now2)
now3 = now.strftime("%d %B %Y, %I:%M:%S %p")
print(now3)

#[small a,b,c,d uses]:-

#(%c)it is print like this day name,month name,day date(Fri Mar  8 09:22:15 2024)
now4=now.strftime("%c")
print(now4)

#(%a)it prints only day name ex:-sun,mon,sat,fri like this:-
now5=now.strftime("%a")
print(now5)

#(%b)it prints only month name ex:-jan,feb,oct like this 
now6=now.strftime("%b")
print(now6)

#(%d)it prints only day ex:-01and 02 and 03 like this:-
now6=now.strftime("%d")
print(now6)

#(%e) it is also print day but it not print 01,02 it print like 1,2,3 ex:-1,2,3 like this  
now7=now.strftime("%e")
print(now7)

#(%g)it print only year last two digits if the year is 2024 it prints only 24/ ex:-2021-21,2022-22 like this:-
now8=now.strftime("%g")
print(now8)

#(%h)it print month name like jan , feb / ex:-jan,feb,aug like this :-
now9=now.strftime("%h")
print(now9)

#(%m)it print month number only like 01,02,03 /ex:-01,02,03 like this :-
now10=now.strftime("%m")
print(now10)

#(%p)it print AM or PM /ex:-10 AM and 10 PM like this :-
now11=now.strftime("%p")
print(now11)

#(%x)it print first month , date , year (03/08/24) like this :-
now12=now.strftime("%x")
print(now12)

#(%y)it print only year 2021,2022 ,2024 like this :-
now13=now.strftime("%Y")
print(now13)

#[capital A,B,C uses]:-

#(%A) it print day full name / ex:-sunday,monday like this :- 
now14=now.strftime("%A")
print(now14)

#(%B) it print month full name ex:- january,febru,ry,march like this :-
now15=now.strftime("%B")
print(now15)

#(%C) it print year forst two digits if the year 1990 it print only 19 and 
#if year 2024 it print only 20 like this :-
now17=now.strftime("%C")
print(now17)

#(%D)it print whole date / ex:-03/08/24 like this :-
now16=now.strftime("%D")
print(now16)


#(%F)it print year,month,day / ex:-20024-03-08 like this :-
now16=now.strftime("%F")
print(now16)

#(%G)it print only year / ex:-2023 , 2024 like this :-
now17=now.strftime("%G")
print(now17)

#(%X)it print time / ex:-09:56:48 like this :-
now18=now.strftime("%X")
print(now18)

#(%Y) it print year only / ex:-2022,2023,2024 like this :-
now19=now.strftime("%Y")
print(now19)

print("_____________________________________________________________________")
#import calendar:-
import calendar

# it prints whole year calendar:-
year=2024
month=3
print(calendar.calendar(year,month))

# it print only month:-
import calendar
year=2024
month=3
print(calendar.month(year,month))
