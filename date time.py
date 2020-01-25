# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:58:42 2020

@author: DS7_RVepuri
"""

import calendar as c
from datetime import *
import time
#1.Write a Python script to display the Current date and time
tday =date.today()
print(tday)

time = datetime.time(datetime.now())
print(time)

"""Current year"""
print('Current Year', tday.year)

"""Month of year"""
print('Current Month', tday.month)

"""Week number of the year"""
print('Current Week', tday.isocalendar()[1])

""" Weekday of the week"""
print('Current Weekday', tday.weekday)

"""Day of year"""
print('day of year', tday.strftime('%j'))

"""Day of the month"""
print('day of month', tday.strftime('%m'))

"""Day of week"""


#2. Write a Python program to determine whether a given year is a leap year
print(c.isleap(int(input("Enter the Year\n"))))

#3.Write a Python program to convert a string to datetime.
date1 = datetime.strptime('Jul 1 2020 2:43PM', '%b %d %Y %I:%M%p')
print(date1)

#4.Write a Python program to get the current time in Python
today=datetime.now()
print(today)

#5.Write a Python program to subtract five days from current date.
dt = date.today() - timedelta(5)
print(dt)

#6.Write a Python program to convert unix timestamp string to readable date.
dt1 = datetime.fromtimestamp(int("1284105682")).strftime('%Y-%m-%d %H:%M:%S')
print(dt1)

#7.Write a Python program to print yesterday, today, tomorrow.
today = date.today()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1) 
print('Yesterday : ',yesterday)
print('Today : ',today)
print('Tomorrow : ',tomorrow)

#8.Write a Python program to convert the date to datetime (midnight of the

print(datetime.combine(today, datetime.min.time()))

#9.Write a Python program to print next 5 days starting from today"""

for i in range(1,6):
    Nextday = today + timedelta(days = i) 
    print(Nextday)
    
#10.Write a Python program to add 5 seconds with the current time"""
today = datetime.now()
print(today)
addtime = today + timedelta(seconds = 5)
print(addtime)

#11. Write a Python program to convert Year/Month/Day to Day of Year
day_of_year = (today - datetime(today.year,1,1)).days+1
print(day_of_year)

#12.Write a Python program to get current time in milliseconds in Python
print(today.strftime('%f'))

#13.Write a Python program to get week number.
print(datetime.date(2015, 6, 16).isocalendar()[1])

#14.Write a Python program to find the date of the first Monday of a given week
print(time.asctime(time.strptime('2020 45 1', '%Y %W %w')))

#15.Write a Python program to select all the Sundays of a specified year.

def all_sundays(year):
# January 1st of the given year
       dt = date(year, 1, 1)
# First Sunday of the given year       
       dt += timedelta(days = 6 - dt.weekday())  
       while dt.year == year:
          yield dt
          dt += timedelta(days = 7)
for s in all_sundays(2020):
    print(s)
    
#16.Write a Python program to get days between two dates
a = date(2020,2,28)
b = date(2021,2,28)
print(b-a)

#17.Write a Python program to get the date of the last Tuesday.
today = date.today()
print(today)
offset = (today.weekday() - 1) % 7
print(offset)
last_tuesday = today - timedelta(days=offset)
print(last_tuesday)

#18.Write a Python program to get the last day of a specified year and month
year = 2021
month = 3
print(c.monthrange(year, month)[1])

#19.Write a Python program to get the number of days of a given month andyear

print(c.monthrange(year,month))

#20.Write a Python program to convert a date to the timestamp.
now = datetime.now()
print(now)
print(time.mktime(now.timetuple()))
print()

#21.Write a Python program to convert a string date to the timestamp"""

s = "01/10/2016"
print(time.mktime(datetime.strptime(s, "%d/%m/%Y").timetuple()))

#22. Write a Python program to convert two date difference in days, hours,minutes, seconds.
def date_diff_in_seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def dhms_from_seconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

#Specified date
date1 = datetime.strptime('2019-12-12 01:00:00', '%Y-%m-%d %H:%M:%S')

#Current date
date2 = datetime.now()

print("\n%d days, %d hours, %d minutes, %d seconds" % dhms_from_seconds(date_diff_in_seconds(date2, date1)))

round(5.5)
