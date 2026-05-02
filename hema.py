name="HEMASHREE"
n=int(input("enter size:"))
for row in range(n):
    for ch in name:
        for col in range(n):
            if ch=="H":
                if col==0 or col==n-1 or row==n//2:
                    print("#",end=" ")
                else:
                    print(" ",end=" ")
            elif ch=="E":
                if row==0 or row==n-1 or row==n//2 or col==0:
                    print("#",end=" ")
                else:
                    print(" ",end=" ")
            elif ch=="M":
                if col==0 or col==n-1 or (row==col and row<=n//2) or (row+col==n-1 and row<=n//2):
                    print("#",end=" ")
                else:
                    print(" ",end=" ")
            elif ch=="A":
                if col==0 or col==n-1 or row==0 or row==n//2:
                    print("#",end=" ")
                else:
                    print(" ",end=" ")
            elif ch=="S":
                if row==0 or row==n-1 or row==n//2 or(row<=n//2 and col==0) or (row>=n//2 and col==n-1):
                    print("#",end=" ")
                else:
                    print(" ",end=" ")
            elif ch=="R":
                if row==0 or col==0 or row==n//2 or(row<=n//2 and col==n-1) or (row==col and row>=n//2):
                    print("#",end=" ")
                else:
                    print(" ",end=" ")
        print(" ",end=" ")
    print()
