# print("Hello, World!")

# Types of variables in Python
x = 5  # Integer
y = 3.14  # Float
z = "Hello"  # String
p = True  # Boolean
q = "3.12"

# Type casting
newY = int(y) # Output : 3 Loss of precison
newX = float(x)
newXStr = str(x) 
# newZ = float(z)  # Error
newZStr = float(q) # No error
# newZStr2 = int(newZStr) # No error
newZStr2 = int(float(q)) 

boolInt = -1 # 0 Anytghing non Zero is True and zero is false
boolVal = bool(boolInt) # True

boolInt2 = 2
boolVal2 = bool(boolInt2) # True

# String "", '' and ''' '''

print("Integer:", x)
print("Float:", y)
print("String:", z)
print("Boolean:", p)
print("Float as Integer:", newY)
print("Integer as Float:", newX)
print("Integer as String:", newXStr)
print("String as Integer:", newZStr)
print("String as Float:", newZStr2)
print("Boolean as Integer:", boolVal)
print("Boolean as Float:", boolVal2)
# print("String as float:", newZ)