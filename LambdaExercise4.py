import datetime
present = datetime.datetime.now()
print(present)

year = lambda x:x.year
month = lambda x:x.month
day = lambda x:x.day 
time = lambda x:x.time() 

print("Current year:",year(present))
print("Current month:",month(present))
print("Current day:",day(present))
print("Current time:",time(present))

