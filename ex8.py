# "%r" can read any kind of data
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
# True and False are built-in keywords that don't need quotes
print formatter % (True, False, False, True)
# Reads the formatter variable literally as text.
print formatter % (formatter, formatter, formatter, formatter)
# This is split up so it doesn't go over 80 characters in a line.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
