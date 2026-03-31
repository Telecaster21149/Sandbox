def access_level(age):
    if age >= 18:
        return "adult"
    else:
        return "minor"
print("age_16:", access_level(16))
print("age_18:", access_level(18))
print("age_21:", access_level(21))
