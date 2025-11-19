# LD 2nd Squared Numbers Practice

#Establish list of numbers
nums = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]
# Use map and lambda to loop over list and square numbers
squared = list(map(lambda num: num**2, nums))
# Print both original number and its squared value
for i, num in enumerate(nums):
    print(f"Original: {num}, Squared: {squared[i]}")