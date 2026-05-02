#num=int(input("enter the number:"))
#i=2
#while i<num:
#    if num%i==0:
#        print("not prime")
#        break
#    i+=1
#else:
#    print("prime")
for num in range(10,61):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)

#for i in range(100):
#    if i%3==0:
#        pass
#    else:
#       print(i)