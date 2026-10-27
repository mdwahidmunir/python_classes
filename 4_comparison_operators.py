# Comparison operators in Python
# ==, !=, >, <, >=, <=

# Numeric examples
x = 10
y = 20
z = 10

print("x == y:", x == y)      # False
print("x == z:", x == z)      # True
print("x != y:", x != y)      # True
print("x > y:", x > y)        # False
print("x < y:", x < y)        # True
print("x >= z:", x >= z)      # True
print("y <= x:", y <= x)      # False

# String examples
name1 = "Alice"
name2 = "Bob"
name3 = "Alice"

print("name1 == name2:", name1 == name2)  # False
print("name1 == name3:", name1 == name3)  # True
print("name1 != name2:", name1 != name2)  # True
print("name1 < name2:", name1 < name2)    # True (lexicographical order)

# Comparison results are boolean values
print(type(x < y))
