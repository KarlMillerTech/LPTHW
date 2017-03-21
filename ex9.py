# assigns the variable days with a string of the days of the week.
days = "Mon Tue Wed Thu Fri Sat Sun"
# \n places each following part of a string on a new line.
# But \n is printed literally with %r
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# prints the days and months.
# Comma adds a space
print "Here are the days:", days
print "Here are the months: ", months

# three double quotes prints out a string which spans multiple lines.
#  The initial """ needs to be on the
# same line as "print"
# Triple quotes also add a new line at beginning and end.
# And no spaces between like " " "
print """
There's something going on here.
With three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
