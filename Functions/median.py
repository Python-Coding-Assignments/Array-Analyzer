def getMedian(array, SIZE):
    """This function returns the median value of the list."""
    
    #conditional statement which checks to see if the length of the list is odd
    if SIZE % 2 == 1:
        #returning a string value of the median, accurate to one decimal position
        return "{:.1f}".format(array[int((SIZE / 2) - 0.5)])
    #conditional statement which checks to see if the length of the list is even
    else:
        #returning a string value of the median, accurate to one decimal position
        return "{:.1f}".format(0.5 * (array[int((SIZE / 2) - 1)] + array[int(SIZE / 2)]))