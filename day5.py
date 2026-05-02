#import arith
#print(arith.sqrt(5,2))

#a=5
#print(type(a))
#class Building:
#    pass

#Building1=Building()
#print(type(Building1))

#class computershop:
#    def __init__(self,r,h):
#        self.ram=r
#        self.hdd=h
#    def poweron(self):
#        print("computer Switched on...")
#    def config(self):
#        print(f"{self.ram} of Ram and {self.hdd} of HDD")
#com1=computershop("8 GB","500 GB")
#computer.poweron(com1)
#com1.poweron()
#com1.config()

#com2=computershop("32 GB ","1 TB")
#com2.config()

#class student:
#    def data(self):
#        self.name=input("enter name:")
#        self.reg=int(input("enter num:"))
#        self.m1=int(input("enter m1 marks:"))
#        self.m2=int(input("enter m2 marks:"))
#        self.m3=int(input("enter m3 marks:"))
#    def average(self):
#        self.average=self.m1+self.m2+self.m3/3
#    def display(self):
#        print("name",self.name)
#        print("reg",self.reg)
#        print("marks",self.average)
#s=student()
#s.data()
#s.average()
#s.display()
    

class student():
    def __init__(self,name,reg,m1,m2,m3):
        self.name=name
        self.reg=reg
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return((self.m1+self.m2+self.m3)/3)
count=int(input("how many students:"))
st_list=[]
for i in range(count):
    name=input("student name:")
    reg=int(input("reg no:"))
    m1=int(input("mark 1:"))
    m2=int(input("mark 2:"))
    m3=int(input("mark 3:"))
    st=student(name,reg,m1,m2,m3)
    st_list.append(st)

for stud in st_list:
    print(f"{stud.name}:{stud.avg()}")