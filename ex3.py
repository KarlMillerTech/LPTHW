# outputs (prints) a string
print "I will now count my chickens:"

# prints a string followed by a calculation
# 1. 30 /6 = 5
# 2. 25 + "5" = 30
# Quote are just for emphasis.

print "Hens", 25.0 + 30.0 / 6

# 1. 25 * 3 = 75
# 2. 75 % 4 = 3 (because 75/4 = 18 r 3)
# 3. 100 - "3" = 97
print "Roosters", 100.0 - 25.0 * 3 % 4

# see line 1
print "I will now count the eggs:"

# 1. 4 % 2 = 0 (because 4/2 has no remainded)
# 2. 1.0 / 4 = 0.25 (need the .0 to make floating point)
# 3. The add and subtract left to right:
#    3 + 2 + 1 - 5 + "0" - "0.25" + 6 = 6.75
#    (I used quotes to emphasise don't use them in code)
print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0

# Is 5 < -2?
print "Is it true that 3 + 2 < 5 - 7?"

# will return False because 3 + 2 is NOT less than 5 - 7
print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

# will return True because 5 is greater than - 2
print "Is it greater?", 5 > -2
# will return True because 5 is greater than or equal to -2
print "Is it greater or equal?", 5 >= -2
# returns False because 5 is NOT less than or equal to -2
print "Is it less or equal?", 5 <= -2

print 7.0 / 4.0

# I added these last few lines

print
print "These show math with integers vs. floating point numbers"

print "5 / 4 =", 5 / 4, "(The .25 got truncated)"
print "5.0 / 4 =", 5.0 / 4
print "5 / 4.0 =", 5 / 4.0
print "5.0 / 4.0 =", 5.0 / 4.0
