# LD 2nd For Loops Notes
import time

nums = [6,652,5,76535,57,637,63567,35,7,5,3,11,46,5,25697]

for num in nums:
    div = num / 2
    if div > 100:
        print(f"{div} is half of {num} and it is still a large number!")
    else:
        print(num)

print("We completed all the numbers!")
time.sleep(3)

for x in range(1,10):
    print(x)
time.sleep(3)

print("Count by Twos:")
for x in range(2,11,2):
    print(x)
time.sleep(3)

print("Count down")
for x in range(10,0,-1):
    print(x)
    time.sleep(1)