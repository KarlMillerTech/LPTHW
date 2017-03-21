# This adds an "import" that adds functions to Python.
# The functions constitute a "module" of code.
# (Modules can also be called "libraries.")
# "argv" is the "argument variable" that holds
# variables that you send in (or "pass") to Python
from sys import argv

# This line "unpacks" argv into four variables from
# left to right.
script, first, second, third = argv

# Each prints a string followed by the user assigned variables.
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
# prints the last three user inputed variables.
print first, second, third

# When you run this script, type the information for
# the variables on the same line as "python ex13.py"
# like these two examples:
# $ python ex13.py karl learns progrmamming
# $ python ex13.py zed writes books
# (Remember that the script name, "ex13.py" is the
# first variable, called "script" in this example.)
