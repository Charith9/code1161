"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# This creates a list.
some_words = ['what', 'does', 'this', 'line', 'do', '?'] # The words are listed one by one.

# To find and print out the the string "word" from the list "some_words"
for word in some_words:
    print(word) # Nothing happens as there is no "word" in "some_words"

# Same case as above, tries to find the string "x" in "some_words"
for x in some_words:
    print(x) # "x" is not available so nothing is printed.

# Prints out the list "some_words"
print(some_words) # "some_words" is listed out

# Checks to see if the length of the list is more than 3, if it is then the print command is carried out.
if len(some_words) > 3:
    print('some_words contains more than 3 words') # Print command takes place and displays "some_words contains more than 3 words"

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
