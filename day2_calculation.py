x=int(input("Give me your number:"))
y=int(input("Give me your number:"))
z=input("Give me your function(+,-,*,/):")

def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def mul(x,y):
    print(x*y)
def div(x,y):
    print(x/y)
    
if z=="+":
    add(x,y)
elif z=="-":
    sub(x,y)
elif z=="*":
    mul(x,y)
elif z=="/":
    div(x,y)

