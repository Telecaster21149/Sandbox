def greet(name, age):
    return f"Name: {name}, age: {age}"
a = greet("Danya", 25)
b = greet(age=25, name="Danya")
print("positional:", a)
print("named:", b)
print("same_result:", a == b)
