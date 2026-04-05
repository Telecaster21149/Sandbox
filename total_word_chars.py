def total_word_chars(text):
    words = text.strip().split()
    total = 0
    for word in words:
        total += len(word)
    return total
print("chars_1:", total_word_chars("hello world"))
print("chars_2:", total_word_chars("  hi   python world  "))
print("chars_3:", total_word_chars(""))
print("chars_4:", total_word_chars("   "))
