# LD 2nd Average Grade

#Get input of number of classes
num_of_classes = int(input("How many classes do you have: \n"))

#Array of the name of the classes
classes = []
for x in range(num_of_classes):
    class_name = input(f"What is the class name for your {x+1} class: \n")
    classes.append(class_name)


#Loop through array asking for the grade (Float)
grades = []
for y in classes:
    grade = float(input(f"What is your grade in {y}:\n"))
    grades.append(grade)


#average out the grades
average = sum(grades) / len(grades)

print("The average grade between all of your classes is:", average)