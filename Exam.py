score1=input("please enter คะแนน1 ")
while True:
    if score1== "W":
        print("ติด ร")
        break
    score11=int(score1)
    break
score2=int(input("please enter คะแนน2 "))
score3=int(input("please enter คะแนน3 "))
score4=int(input("please enter คะแนน4 "))
score=score11+score2+score3+score4
if score >=80:
    grade="4"
elif score >= 79:
    grade="3.5"
elif score >= 74:
    grade="3"
elif score >= 69:
    grade="2.5"
elif score >= 64:
    grade="2"
elif score >= 59:
    grade="1.5"
elif score >= 54:
    grade="1"
else:
    grade="0"
print("Your grade is",grade)