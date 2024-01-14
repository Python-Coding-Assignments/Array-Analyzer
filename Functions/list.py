import random

def generateList(min, max, SIZE):
    """This function generates an array, either randomly or with chosen values.  The function appends the elements to the end of a list.  Afterwards, the function then returns the list."""

    #declaration and initialization of variables
    array = []
    userInput = ""
    value = False
    arrayElement = 0

    #while loop which runs until until a complete list is generated
    while value == False:
        #prompting user to enter either c, C, r, or R
        userInput = input("Enter (c)ustom or (r)andom values? --> ")

        #conditional statement which checks if user input is either r or R
        if userInput == "r" or userInput == "R":
            #for loop which runs SIZE number of times
            for i in range(0, SIZE):
                #appending randomly assigned value to end of list
                array.append(random.randint(min, max))
            value = True

        #conditional statement which checks if user input is either c or C
        elif userInput == "c" or userInput == "C":
            print("Enter " + str(SIZE) + " numbers:")
            #for loop which runs SIZE number of times
            for i in range(0, SIZE):
                #prompting user to input SIZE number of integers
                arrayElement = int(input("Element at index " + str(i) + ": "))
                #appending newly entered value to end of list
                array.append(arrayElement)
            value = True

    #returning local list called array
    return array        