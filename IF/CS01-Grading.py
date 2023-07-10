scorekab=int(input("please enter คะแนนเก็บ"))
if scorekab <= 30:
    print("Ok")
else:
    print("invalid")
scoreklang=int(input("please enter คะแนนสอบกลางภาค"))
if scoreklang <= 30:
    print("Ok")
else:
    print("invalid")
scorepluy=int(input("please enter คะแนนสอบปลายภาค"))
if scorepluy <= 40:
    print("Ok")
else:
    print("invalid")
score=scorekab+scoreklang+scorepluy
if score >=80:
    grade="A"
elif score >= 79:
    grade="B+"
elif score >= 74:
    grade="B"
elif score >= 69:
    grade="C+"
elif score >= 64:
    grade="C"
elif score >= 59:
    grade="D+"
elif score >= 54:
    grade="D"
else:
    grade="F"
print("Your grade is",grade)

