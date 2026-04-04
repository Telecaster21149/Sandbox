def count_items(items):
    count = 0
    for item in items:
        count += 1
    return count
print("count_3:", count_items(["a", "b", "c"]))
print("count_1:", count_items(["x"]))
print("count_0:", count_items([]))
