def sum_even(items):
    total = 0
    for item in items:
        if item % 2 == 0:
            total += item
    return total
print("sum_even_1:", sum_even([2, 4, 5, 7, 8]))
print("sum_even_2:", sum_even([1, 3, 5]))
print("sum_even_3:", sum_even([]))
