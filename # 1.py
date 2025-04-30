# 1
first = "Hello World"

# 2
# This is a comment.

# 3
print("I AM A COMPUTER!")

# 4
if 1 < 2 and 4 > 2:
    print("Math is fun.")

# 5
nope = None

# 6
result = True and False
print("Result of True and False:", result)

# 7
length = len("What's my length?")
print("Length:", length)

# 8
shouting = "i am shouting".upper()
print(shouting)

# 9
number = int("1000")
print(number)

# 10
combined = str(4) + "real"
print(combined)

# 11
print(3 * "cool")  

# 12
try:
    crash = 1 / 0
except ZeroDivisionError:
    print("ZeroDivisionError")

# 13
print(type([]))  

# 14
name = input("What's your name? ")

# 15
try:
    user_number = float(input("Enter a number: "))
    if user_number < 0:
        print("That number is less than 0!")
    elif user_number > 0:
        print("That number is greater than 0!")
    else:
        print("You picked 0!")
except ValueError:
    print("Please enter a valid number.")

# 16
print("apple".index("l")) 

# 17
print("y" in "xylophone")  

# 18
my_string = "example"
print(my_string.islower())  # True
