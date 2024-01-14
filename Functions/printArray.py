def getArray(array, SIZE):
    """This function prints the list out in a nice fashion."""
    
    #for loop which runs SIZE times
    for i in range(0, SIZE):
        #conditional statement which checks whether i is one less than SIZE
        if i < SIZE - 1:
            print(str(array[i]), end= ", ")
        #conditional statement which checks whether i is equal to one less than SIZE    
        else:
            print(str(array[i]))    