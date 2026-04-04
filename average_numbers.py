def average_numbers(items):
    if not items:
        return 0
    total = 0
    for item in items:
        total += item
    return total / len(items)
print("avg_1:", average_numbers([2, 4, 6]))
print("avg_2:", average_numbers([10, 20]))
print("avg_3:", average_numbers([]))

