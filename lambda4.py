import datetime
now = datetime.datetime.now()

year = lambda x: x.year
print(year(now))

month = lambda x: x.month
print(month(now))

day = lambda x: x.day
print(day(now))

t = lambda x: x.time()
print(t(now))