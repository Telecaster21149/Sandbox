def grade(score):
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    else:
        return "C"


print("score_95:", grade(95))
print("score_75:", grade(75))
print("score_40:", grade(40))
