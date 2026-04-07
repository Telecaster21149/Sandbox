def normalize_text(text):
    words = text.lower().strip().split()
    return " ".join(words)
if __name__ == "__main__":
    print("norm_1:", repr(normalize_text("  HeLLo   PyThOn  WoRLD  ")))
    print("norm_2:", repr(normalize_text("ONE   two")))
    print("norm_3:", repr(normalize_text("")))
    print("norm_4:", repr(normalize_text("   ")))
