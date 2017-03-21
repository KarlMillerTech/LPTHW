from sys import argv

# Must enter name after python ex14.py xxx and run.
script, user_name = argv
prompt = '> '

# Takes the raw_input given at the prompt and returns it.
# Zed calls "%" here the "format activator"
# It is also called the string formatting operator
# or the interpolation operator (when in the code)
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
# Stored variables can be over-written by a user.
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
# Takes the raw_input given by the user and assigns a variable.
# In this case whatever the user inputs gets fed back to them after the prompt >
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print '''
Alight, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice!
''' % (likes, lives, computer)
