# Objectives
# Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

# Create an if statement that includes both elif and else to execute when both if and elif are not met.

print("enter two numbers")
a=input("Enter a number for a ")
b=input("Enter a number for b ")
if (a == b) and (b == a):
    print("a equals b")
elif (a < b) and (b >=a):
    print("a is less than b")
else:
    print("a is greater than b")