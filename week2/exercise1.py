"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# dictionary of words
some_words = ['what', 'does', 'this', 'line', 'do', '?']
# prints all words
for word in some_words:
    print(word)     #printed the words in a for loop
# there is no variable x so it wont print anything
for x in some_words:
    print(x)        #added x as a variable to be used in some_words
# will print some words
print(some_words)   #printed in bracket format
# if the length of some_words is greater than 3 itll print
if len(some_words) > 3:
    print('some_words contains more than 3 words')  # printed

def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
