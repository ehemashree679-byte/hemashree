num=int(input("enter the number from user:"))
temp=num
sum=0
while num>0:
    last=num%10
    sum=sum+last**3
    numk=num//10
if temp==sum:
    print("it is armstong")
else:
    print("it is not armstrong")
    