def count_even(items):
    count = 0
    for item in items:
        if item % 2 == 0:
            count += 1
    return count
print("even_1:", count_even([2, 4, 5, 7, 8]))
print("even_2:", count_even([1, 3, 5]))
print("even_3:", count_even([]))
