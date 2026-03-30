def hello(name):
    print("Hello,", name)


def add(a, b):
    return a + b


print("direct_add:", add(2, 3))

result = add(5, 7)
print("saved_add:", result)

print("hello_return:", hello("Danya"))
