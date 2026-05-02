#enter the number
num1=int(input("enter the number:"))
#number is divisible by 3 and 5 print welcome
if num1%3==0 and num1%5==0:
    print("welcome")
    # number divisible by 5 print hello
elif num1%5==0:
    print("hello")
    #number divisible by 3 print hi
elif num1%3==0:
    print("hi")
    #number is not divisible by 5 and 3 print quiet
else:
    print("quiet")