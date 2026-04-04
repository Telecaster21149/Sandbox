def total_chars(items):
    total = 0
    for item in items:
        total += len(item)

    return total
print("chars_1:", total_chars(["a", "bb", "ccc"]))
print("chars_2:", total_chars(["hello", "yo"]))
print("chars_3:", total_chars([]))

