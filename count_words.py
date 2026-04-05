def count_words(text):
    words = text.strip().split()
    return len(words)
print("words_1:", count_words("hello world"))
print("words_2:", count_words("  hello   python world  "))
print("words_3:", count_words(""))
print("words_4:", count_words("   "))
