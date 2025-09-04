# LD 2nd String Methods Notes

name = input("What is your name:\n").strip().title()
age = float(input("How old are you:\n"))

print("Hello {} it's nice to meet you! I can't believe you are {:.2f}!".format(name, age))

print(f"Hello {name} it's nice to meet you! I can't believe you are {age:.1f}!")



#print(age.isdigit())

#print("Really? " + age + " is old.")

sentance = "The quick brown fox jumps over the lazy dog!"

word = "brown"
start = sentance.find(word)
length = len(word)


#print(sentance.replace(word, "yellow"))