import datetime
import calendar
import os
import webbrowser




courses = ['History', 'Math', 'Physics', 'CompSci']

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))
print(os.getcwd())
print(os.__file__)
webbrowser.open("https://xkcd.com/353/")