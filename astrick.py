n=int(input("enter the num:"))
for row in range (n):
    for col in range (n):
        if row==0 or row==n-1 or row==2 : 
            print("#",end=" ")
        elif row<n//2 and col==0:
            print("#",end=" ")
        elif row>n//2 and col==n-1:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()