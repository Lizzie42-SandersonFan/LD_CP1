# LD 2nd Squared Numbers Practice

nums = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]
squared = list(map(lambda num: num**2, nums))
for i, num in enumerate(nums):
    print(f"Original: {num}, Squared: {squared[i]}")