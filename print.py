n=int(input("enter the num:"))
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or col==0 or col==n-1:
            print("#",end=" ")
            
        else:
            print(" ",end=" ")
    print()
    


n=int(input("enter the num:"))
for j in range(n):
    for i in range(n):
        print("#",end=" ")
    print()

n=int(input("enter the num:"))
for i in range(n):
    print("#",end=" ")

num=int(input("enter the num:"))
i=1
while i<=10:
    print(f"{i}*{num}={i*num}")
    i+=1
