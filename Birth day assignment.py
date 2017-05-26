Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import calendar
>>> age = int (input ("Enter Your age:"))
Enter Your age: 20
>>> date = int (input ("Enter your date of birth:"))
Enter your date of birth: 17
>>> month = int (input("Enter your month of birth(1-12):"))
Enter your month of birth(1-12): 7
>>> currentyear = int(input("Enter your current year:"))
Enter your current year: 2017
>>> year=currentyear-age
>>> weekday=calendar.weekday(year,month,date)
>>> dayofweek=calendar.day_name[weekday]
>>> monthstring=calendar.month_name[month]
>>> print("you were born on a "+ str(date)+ " " + monthstring + " " +str(year) + " on a " + dayofweek)
you were born on a 17 July 1997 on a Thursday
>>> 
