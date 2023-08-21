num=1
while True:
    user=int(input("Enter number "))
    if user==0:
        print(num-1)
        break
    print(num)
    num=num+1