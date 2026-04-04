def filter_even(items):
    result = []
    for item in items:
       if item % 2 == 0:
            result.append(item)
    return result
print("filtered_1:", filter_even([2, 4, 5, 7, 8]))
print("filtered_2:", filter_even([1, 3, 5]))
print("filtered_3:", filter_even([]))

