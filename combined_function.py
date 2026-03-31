def profile(name, age, greeting="Hello"):
    if age >= 18:
        status = "adult"
    else:
        status = "minor"
    return f"{greeting}, {name} ({status})"
print("case_1:", profile("Danya", 25))
print("case_2:", profile("Misha", 16))
print("case_3:", profile("Anna", 19, "Welcome"))
