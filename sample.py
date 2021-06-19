import time
import datetime

dt_now = datetime.datetime.now()

yesterday = datetime.datetime(dt_now.year, dt_now.month, dt_now.day-1, 10)
today = datetime.datetime(dt_now.year, dt_now.month, dt_now.day, 10)
print("after:" + str(int(time.mktime(yesterday.timetuple()))) +
      " before:" + str(int(time.mktime(today.timetuple()))))
