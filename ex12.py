# prompts user in terminal to input data.
age = raw_input("How old are you? ")
# prompts user in terminal to input data.
height = raw_input("How tall are you? ")
# prompts user in terminal to input data.
weight = raw_input("How much do you weigh? ")

# gets the values of the user input and displays them in a string.
# split up lines so that they're less than 80 characters.
print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# At shell prompt, type "pydoc raw_input" (w/o quotes)
# Type "q" to quit and return to shell prompt
# Also try
#    pydoc open  # compare "man open"
#    pydoc file  # compare "man file"
#    pydoc os    # no entry in "man"
#    pydoc sys   # no entry in "man"
