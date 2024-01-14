import Constants.constants as constants
from Functions import getHighestFrequency, generateList, getMedian, getArray, getSorted

#declaration in initialization of variable
array = []

#function call which generates a list which will be assigned to local list called array
array = generateList(constants.minimum, constants.maximum, constants.size)
#function call which prints the user's list
print("\nArray Analysis:\n----------------------------\nYour array:", end= " ")
getArray(array, constants.size)

#function call to get minimum value within list
print("\nMinimum: " + str(min(array)))
#function call to get maximum value within list
print("Maximum: " + str(max(array)))
#function call to get sum of all elements of the list
print("Sum: " + str(sum(array)))

#function call to sort the list in increasing order
print("Sorted array:", end= " ")
getSorted(array, constants.size)

#function call to get median value within list
print("Median: " + str(getMedian(array, constants.size)))
#function call to get highest frequency value within list
getHighestFrequency(array, constants.size)