n=int(input("enter the num:"))
mid=n//2
left,right=mid,mid

for row in range(n):
    for col  in range (n):
        if col==left or col==right :
            print("#",end=" ")
        else:
            print(" ",end=" ")
    if row>=mid:
        left+=1
        right-=1
    else:
        left-=1
        right+=1
    print()
    
    
    
    