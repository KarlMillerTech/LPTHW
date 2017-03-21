# The comma prevents a new line: this way the
# promptfor data shows up on the same line.
# Note that you can put any kind of data in.
print "How old are you?",
# asks user in terminal to input data.
age = raw_input()
print "How tall are you?",
# asks user in terminal to input data.
height = raw_input()
print "How much do you weigh?",
# asks user in terminal to input data.
weight = raw_input()

print # This inserts a blank line in the printout.

# gets the values of the user input and displays them in a string.
# split up lines so that they're less than 80 characters.
print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

print # This inserts a blank line in the printout.

# But if you want to add a little more text to the string,
# wich would push it over 80 characters, you can do this:

print ("So, you're %r years old, %r inches tall, \n"
       "    and %r pounds heavy") % (age, height, weight)

# Adjacent string literals are joined into a single string
# (Just make sure to use parentheses)
# The "\n" is used to break the printout into two lines
# and the leading spaces line up the text.
