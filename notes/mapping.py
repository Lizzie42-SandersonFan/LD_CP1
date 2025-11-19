# LD 2nd Mapping Notes

numbers = [452,6,2563,572,5722,75,2,5,61,457,75]
"""divided = []

for num in numbers:
    divided.append(num/2)"""

"""def divide(number):
    return number/2"""

divided = list(map(lambda num: num/2, numbers))

for i, num in enumerate(numbers):
    print(f"{num} divided by 2 is {divided[i]}")