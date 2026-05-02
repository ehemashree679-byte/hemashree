#PRINT NAME MULTIPLE TIMES
#name=input("enter:")
#count=0
#while count<5:
#    print(name)
#    count+=1

#NATURAL NUMBERS
#start=1
#while start<=100:
#    print(start)
#    start+=1

#NATURAL NUMBERS 
#num=int(input("enter the number :"))
#i=1
#while i<=num:
#    print(i)
#    i+=1

#REVERSE THE NUMBER
#num=int(input("enter:"))
#start=1
#while start<=num:
#    print(num)
#    num-=1

#ODD NUMBERS
#num=int(input("enter :"))
#start=1
#while start<=num:
#    print(start)
#   start+=2

#EVEN NUMBERS
#num1=int(input("enter first number:"))
#num2=int(input("enter seond number:"))
#while num1<=num2:
#    if num1%2==0:
#        print(num1)
#    num1+=1

#sum of natural numbers
#num=int(input("enter the number:"))
#sum = 0
#i =1
#while i<=num:
#    sum=sum+i
#    i+=1
#print(sum)

#table

#num=int(input("enter the number:"))
#i=1
#while i<=10:
#   print(f"{i}*{num}={i*num}")
#   i+=1

num=int(input("enter the number:"))
total=0
while num>0:
    digit=num%10
    total=total+digit
    num=num//10
print(total)


#num=int(input("enter the number:"))
#total=0
#while num>0:
 #  last=num%10
  # total=total*10+last
   #num=num//10
#print(total)


num=int(input("enter the number:"))
original=num
total=0
while num>0:
    last=num%10
    total=total*10+last
    num=num//10
if original==total:
    print("it is palindrome")
else:
    print("not palindrome")

num=int(input("enter the number:"))
fact=1
i=1
while i<=num:
    fact=fact*i
    i+=1
print(fact)
