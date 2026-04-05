text = "  HeLLo PyThOn world  "
lowered = text.lower()
words = text.strip().split()
print("original:", repr(text))
print("lowered:", repr(lowered))
print("words:", words)
print("words_count:", len(words))
