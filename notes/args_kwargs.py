# LD 2nd *args and **kwargs Notes

"""def hello(name="Tia", age=29):
    return f"Hello {name}! You are {age}!"

print(hello())
print(hello("Xavier"))
print(hello("Treyson", 19))"""

def hello(*names, **last):
    for name in names:
        print(f"Hello {name} {last['alast']}")

hello("Alex", "Bob", "Jerry", "Alexa", "Valerie", "Eve", alast="Chris")