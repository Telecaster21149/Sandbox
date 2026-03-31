def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"
print("call_1:", greet("Danya"))
print("call_2:", greet("Danya", "Hi"))
print("call_3:", greet(name="Danya", greeting="Welcome"))
