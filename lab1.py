# Write a multi-line comment with your name, favorite food, and dream job on 3 different lines.
# Corey 
# Pizza
# cyber analyst

# assign 5 different data types to 5 different variables. At least one datatype must be a string.
one = 1
bad = False
name = "Corey Gray"
c = float(1.57)
e = range(5)
# print the length of your string.
print(len(name))

# create a new variable called savvy, and assign it the string with this phrase "Learning Python is Awesome!"

saavy = "learning python is awesome"

# Replace "Awesome" with "great" in the string

saavy = "learning python is great"

# Create and assign 3 more variables called name, age and length using the 

name, age, length = "Corey", 21, 6


# Format a new string called 'miniBio' using variables in curly brackets to complete this phrase... "Hi my name is (name), I am (tall) and (so) old today."

miniBio = (f"Hi my name is {name}, I am {length} and {age} old today.")
print(miniBio)

# Create a list of at least 5 elements of mixed data types
list1 = [6, "python",{"Corey":18}, 3.14 ]

# replace a part of it with something else
list1[2]="age"
print(list1)
# append or insert several more items to the list
list1.append(23)
list1.insert(1, True)
# find and print the length of the list
print(len(list1))
# slice a sub-section of the 1st list, and save it to a different 2nd list
list2=list1[1:2]
# print the 2nd list
print(list2)
# extend your original list with the 2nd list sliced above
list1=list2[1:2]
# Create a new list called "simList" containing at least 5 elements of the same data type, either string, integer, float, or Boolean.
simlist=[1, 71, 1, 23, 42]
# sort "simList", and print the list
simlist.sort()
print(simlist)
# copy the "simList" list to another 3rd list
list3=simlist.copy()
# add the 2nd and 3rd lists together into a 4th list
list4= list2 + list3