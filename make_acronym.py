def make_acronym(text):
    words = text.upper().strip().split()
    letters = []
    for word in words:
        letters.append(word[0])
    return "".join(letters)
if __name__ == "__main__":
    print("acr_1:", make_acronym("hello python world"))
    print("acr_2:", make_acronym("  central processing unit "))
    print("acr_3:", repr(make_acronym("")))
    print("acr_4:", repr(make_acronym("   ")))
