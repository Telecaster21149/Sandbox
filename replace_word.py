def replace_word(text, old, new):
    return text.replace(old, new)
if __name__ == "__main__":
    print("case_1:", replace_word("hello world", "world", "python"))
    print("case_2:", replace_word("one two one", "one", "1"))
    print("case_3:", repr(replace_word("", "a", "b"))) 
