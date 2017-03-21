# imports the argv module. Sometimes called libraries.
from sys import argv

# Uses argv to get a filename.
script, filename = argv

# "open" is a command that reads our text file
# (as long as you put the name of the file in
# the command line when you ran the script)
# Zed says to take a look at "pydoc open"
txt = open(filename)

#Prints a message followed by the selected filename.
print "Here's your file %r:" % filename

# Calls the read function on txt without parameters.
# txt is the variable or object and the . (dot)
# is to add a command, "read" in this case
print txt.read()

# And these do it all over within the script:
print "Type the filename again:"
# Asks the user to input the filename again with the > prompt.
file_again = raw_input("> ")
#Opens the file again.
txt_again = open(file_again)
# Prints the file again.
print txt_again.read()

# Also need to close the files; Zed mentions this
# in the study drills at the bottom of the page.
# Use the file name and the dot operator

txt.close
txt_again.close
