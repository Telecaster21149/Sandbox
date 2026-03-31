def build_message(name):
    text = f"Hello, {name}"
    return text
msg = build_message("Danya")
print("returned:", msg)
try:
    print("outside_text:", text)
except NameError as e:
    print("outside_text_failed:", type(e).__name__)
