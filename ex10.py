# \t makes the string tabbed in.
tabby_cat = "\tI'm tabbed in."
# \n is a new line which will split a string.
persian_cat = "I'm split\non a line."
# \ is an escape character \\ prints \
backslash_cat = "I'm \\ a \\ cat."
# * serves as an asterisk
# Can also put first line with opening quotes
# and last line with closing quotes.
# Can also use triple single quotes: '''
# And with triples.
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
# Each line prints the variables.
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
