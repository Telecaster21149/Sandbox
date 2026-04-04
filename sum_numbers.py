def sum_numbers(items):
    total = 0
    for item in items:
        total += item
    return total
print("sum_1:", sum_numbers([2, 4, 6]))
print("sum_2:", sum_numbers([10, 0, 5]))
print("sum_3:", sum_numbers([]))
