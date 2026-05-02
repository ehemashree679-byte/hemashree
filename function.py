#ARGUMENTS

#positional arguments
#def add(a,b,c):
#   print(f"a is {a} and b is {b} and c is {c} ")

#add(5,6,7)

#variable arguments
#def add(*b):
#    print(sum(b))
#add(5,6,7)

#keyworded arguments
#def login(password,uname):
#   print(f"Name is:{uname}\npassword is: {password}")
#
#login(uname="Logu",password="123")

#keyworded variable length arguments
#def register(age=18,**b):
#    print(b)
#register(uname="shridevi",age=35,mobile=8867092055)


#def register(age=18):
#   print(age)
#register(35)

a=5


def hi():
    a=10
    print(a)
    globals()['a']=15
    def inner():
        print(a)
    inner()

hi()
print(a)