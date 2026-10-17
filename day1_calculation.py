x=int(input("Enter first number:"))
y=int(input("Enter second number:"))

all_x=id(x)
all_y=id(y)
print("The allocation of x=",all_x)
print("The allocation of y=",all_y)

hex_x=hex(x)
hex_y=hex(y)
print("Hex of x:",hex_x)
print("Hex of y:",hex_y)

print("Addition result:",x + y)
print("Multiplition result:",x * y)
if x > y:
    print("Subtraction result:",x - y)
    print("Division result:",x / y)
    
elif x < y:
    print("Subtraction result:",y - x)
    print("Division result:",y / x)