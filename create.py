#enter the units consumed by the user
units=int(input("enter the number of units of electricity consumed:"))
if units<=200:
    print(0)
    #unit is less than and equal to 300 and greater than 200 print num1
elif units<=300:
     bill=(units-200)*1.5
     print(bill)
    #unit is less than and equal to 400 and greater than 300 print num2
elif units<=400:
    #unit is less than and equal to 500 and greater than 400 print num3
     bill=(100*1.5)+(units-300)*3
     print(bill)
    
elif units<=500:
     bill=(100*1.5)+(100*3)+(units-400)*5
     print(bill)
else:
    bill=(100*1.5)+(100*3)+(100*5)+(units-500)*7
    print(bill)