def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"


print("ok_1:", greet("Danya"))
print("ok_2:", greet(greeting="Hi", name="Danya"))
