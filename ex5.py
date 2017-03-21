my_name = 'Karl Miller'
my_age = 29 # the truth
my_height = 74 # inches (not accurate)
my_weight = 180 # lbs (not accurate)
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Red'

# Put % and date type in string (with no space)
# Put %, space, and values after string.
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not that heavy."
# for multiple variables, put in parentheses.
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
# Can do math within a variable list
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

# %s is for "string"
# %d is for "decimal"
# More info at http://j.mp/lfQCwrk
