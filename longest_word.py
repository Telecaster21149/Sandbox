def longest_word(text):
    words = text.strip().split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
if __name__ == "__main__":
    print("longest_1:", longest_word("hi python world"))
    print("longest_2:", longest_word("a ab abc"))
    print("longest_3:", repr(longest_word("")))
    print("longest_4:", repr(longest_word("   ")))
