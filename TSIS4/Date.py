import datetime
from datetime import date, timedelta
# 1
current_day = date.today()
day = date.today() - timedelta(5)

# 2 
yesterday = date.today() - timedelta(1)
tommorov = date.today() + timedelta(1)
print("Today:", date.today())
print("Yesterday:", yesterday)
print("Tomorrow:", tommorov)

# 3 
a = datetime.datetime.now()
b = datetime.datetime.now().replace(microsecond = 0)

# 4 
from datetime import datetime, time
day_z = datetime.strptime('2004-07-07 23:37:24', '%Y-%m-%d %H:%M:%S')
difference = (datetime.now() - day_z)
print(difference.seconds)