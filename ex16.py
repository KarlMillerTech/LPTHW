from sys import argv

script, filename = argv
# Need to include the name of a text file in the
# command line when you run the python script.
# If you are writing or appending (but not reading)
# then a new file will be created with that name
# if one does not already exist.

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
# see "pydoc file" for info
# w = write (vs. r = read, a = append)
# r+ allows you to read AND write
# w+ allows you to write AND read
# r (read only) is default

# Overwrites the text in a file.
print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
# Put in a line break
target.write("\n")
target.write(line2)
# Put in a line break
target.write("\n")
target.write(line3)
# Put in a line break
target.write("\n")

print "And finally, we close it."
target.close()
