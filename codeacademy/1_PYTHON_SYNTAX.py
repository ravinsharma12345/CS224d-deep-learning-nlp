########################### PYTHON SYNTAX ############################
# 1/13 Welcome!
print "Welcome to python"

# 2/13 Variables
spam = 5
my_variable = 10

# 3/13 Booleans
my_int = 7
my_float = 1.23
my_bool = True
my_bool2 = False

# 4/13 Reassignment
my_int = 7
my_int = 3 # reassign to 3
print my_int

# 5/13 and 6/13 Whitespace(indentation) means right space
def spam():
    eggs = 12 # four whitespace to place statement into function
    return eggs # return value of eggs to the caller of spam()

print spam() # call the function

# 7/13 A matter of interpretation
spam = True # Interpreter will run through this code line by line
eggs = False

# 8/13 Single Line Comments
#!mysterious_variable = 42  # Interpreter will ignore comments and will not run them!

# 9/13 Multi-Line Comments
"""
I'm a lumberjack something like that
"""

# 10/13 Math
# Set count_to equal to 1 plus 2 on line 3!
count_to = 1 + 3
print count_to

# 11/13 Exponentiation
#Set eggs equal to 100 using exponentiation on line 3!

eggs = 100 ** 1

print eggs

# 12/13 Modulo
#Set spam equal to 1 using modulo on line 3!

spam =  3 % 2

print spam

# 13/13 Review
#something
monty = True
python = 1.234
monty_python = python ** 2

############################# Tip Calculator ############################
# 1/5 The Meal
# Assign the variable meal the value 44.50 on line 3!

meal = 44.50

# 2/5 The Tax

tax = 6.75 / 100

# 3/5 The Tip
# You're almost there! Assign the tip variable on line 5.

meal = 44.50
tax = 0.0675
tip = 15.0/100


# 4/5 Reassign in a single line
# Reassign meal on line 7!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax


# 5/5 The Total
# Assign the variable total on line 8!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
print("%f" % meal)

total = meal + meal * tip
print("%.2f" % total)