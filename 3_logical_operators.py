# Logical operator examples in Python

# 1. and operator: both conditions must be True
age = 22
has_id = True

if age >= 18 and has_id:
    print("You can enter.")
else:
    print("You cannot enter.")

# 2. or operator: at least one condition must be True
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("You can take a break.")
else:
    print("You need to work.")

# 3. not operator: reverses a boolean value
is_logged_in = False

if not is_logged_in:
    print("Please log in first.")

# 4. Combining logical operators
score = 85

if score >= 50 and score <= 100:
    print("Pass")

if score < 50 or score > 80:
    print("Good result")

# 5. Example with non-boolean values
name = "Alice"
print(name == "Alice" and True)  # True
print(name == "Bob" or False)    # False
print(not (name == "Alice"))     # False
