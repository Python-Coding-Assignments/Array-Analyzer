from Functions import getArray

def getSorted(array, SIZE):
    """This function sorts the list in order from lease to greatest."""

    #this line of code permanently sorts the list from least to greatest
    array.sort()

    #function call which prints the now sorted list in a nice format
    getArray(array, SIZE)