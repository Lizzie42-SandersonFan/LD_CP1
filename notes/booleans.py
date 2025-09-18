# LD 2nd Booleans Notes

import time
import datetime as date

over = False

print(over)

name = -3

print(bool(name))


current_time = time.time()
readable_time = time.ctime(current_time)

print(f"Current Time in seconds since January 1, 1970(epoch time): {current_time}")
print(f"Current Time: {readable_time}")

now = date.datetime.today()
hour = now.strftime("%H")
# Month = %m (%b, %B). Number (writen out)
# Day = %d
# Year = %Y for full or %y for two digit
# Hour = %H
# Minutes = %M
# Seconds = %S

print(f"Current Time according to datetime: {now}")
print(f"Hour: {hour}")
print(f"Hy hour variable is a String: {isinstance(hour, str)}")
print(f"Hy hour variable is a Integer: {isinstance(hour, int)}")
print(f"Hy hour variable is a Float: {isinstance(hour, float)}")