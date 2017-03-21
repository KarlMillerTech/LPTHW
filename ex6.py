# %d places the value of 10 as instructed to at the end.
x = "There are %d types of people." % 10
# creates the variable binary and gives it the value of the string "binary".
binary = "binary"
# creates the variable do_not and gives it the value of the string "don't".
do_not = "don't"
# %s places the values of binary and do_not as instructed to at the end.
y = "Those who know %s and those who %s." % (binary, do_not)

# prints each statement assigned on lines 2 and 8.
print x
print y

# prints a string inside of a string.
# Both of these use variables that use other variables.
print "I said: %r." % x
print "I also said: '%s'." % y

# assigns the boolean of False to the variable hilerious.
hilerious = False
# prints a string inside of a string.
# Zed explains "%r" as standing for "raw data"
# Technically, stands for "repr" or, more fully,
# "a string containing a printable representation
# of an object."
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the variables on lines 19 and 21.
print joke_evaluation % hilerious

# assigns w and e the value of strings.
w = "This is the left side of..."
e = "a string with a right side."

# prints the strings assigned to variables w and e side by side.
print w + e
# Prints with a space between
print w, e
