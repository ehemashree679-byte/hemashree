mark=int(input("enter your marks:"))
if mark>=35:
    print("pass")
    if mark>=90:
        print("medical")
    elif mark>=75:
        print("engineering")
    else :
        print("degree")
else:
    print("fail")
