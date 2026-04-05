def sum_even(items):
    total = 0
    for item in items:
        print("item:", item, "total_before:", total)
        if item % 2 == 0:
            total += item
            print("added:", item, "total_after:", total)
        else:
            print("skipped:", item, "total_after:", total)
    return total
print ("final:", sum_even([2, 4, 5, 7, 8]))
