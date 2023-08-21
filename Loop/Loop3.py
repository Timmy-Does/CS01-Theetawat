count=0
for number in range(int(input("enter number"))):
    if number % 2!=0:
        count +=1
        print(number," ",end ="")