#1. basic keyword arguments
def studentinfo(name,age,city):
    print("name:",name)
    print("age:",age)
    print("city:",city)

studentinfo(age=18,city="rajkot",name="darshit")

#2. mixing positional and keyword
def display(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)

display(1,c=3,b=2)

#3. using keyword arguments
def simple(p:float,r:int,t:float):
    si=(p*r*t)/100
    print("simple interest:",si)

simple_interest(p=10000,t=2,r=1.5)
simple_interest(t=1.5,p=15000,r=2)