import datetime
# mytime = datetime.time(2,20)
# print(mytime.minute)
# print(mytime.hour)
# print(mytime)

# some_day = datetime.date(1993,7,27)
# today = datetime.date.today()
# print(today)
# print(some_day)


# print(today.ctime())
# from datetime import datetime
# mydatetime = datetime(2021,10,3,14,20,1)
# print(mydatetime)

# mydatetime = mydatetime.replace(year=2020)
# # datetime.datetime(2020)
# print(mydatetime)

# you can perform arithmetic on a datetime object
from datetime import date,datetime
# date1 = date(2021, 2,3)
# date2 = date(2020, 11,3)

# result = date1 - date2
# print(result)

# datetime1 = datetime(2021, 2, 3, 22, 20)
# datetime2 = datetime(2020, 11, 3, 11, 20)

# mydiff = datetime1 - datetime2
# print(mydiff)
# print(mydiff.seconds)
# print(mydiff.microseconds)


# date_str = '09-19-2018'
# date_str = '21:30:54'



# date_object = datetime.strptime(date_str, '%H:%M:%S').time()
# print(type(date_object))
# print(date_object) 

# PYTHON DEBUGGER
import pdb
a = [1,2,3]
x = 6
y = 5

print(x + y)
pdb.run(a + y)


