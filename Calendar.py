import calendar

print (calendar.weekheader(3))
print("")
print(calendar.month(2020,3))
print(calendar.monthcalendar(2020, 2))
#this is in more scalar form. Here the 2 is basically
print(calendar.calendar(2020))
print("")
day_of_week=calendar.weekday(2020,9,21)
print(day_of_week)
#In python days start from monday and it is considered 0
leap_check=calendar.isleap(2020)
print(leap_check)
leap_days_count=calendar.leapdays(2000,2004)
print(leap_days_count)
#the lower limit that 2005 won't be inclusive.so make it n+1 o=in order to save it.
