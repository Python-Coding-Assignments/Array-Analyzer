def getHighestFrequency(array, SIZE):
    """This function finds the value which appears the most within the list.  Afterwards, the function prints the highest frequency count found and shows the values that appear that highest frequency number of times."""

    #declaration and initialization of variables
    dictionary = {}
    maxFrequency = 0
    takenIndices = []

    #for loop which iterates over each integer between 0, inclusive, and SIZE, exclusive
    for i in range(0, SIZE):
        #for loop which iterates over each integer between 0, inclusive, and SIZE, exclusive
        for j in range(0, SIZE):
            #conditional statement which checks if list values at indices i and j are equivalent, only if i and j are not equal to each other, and if the list element at index i is not found in the local dictionary
            if array[i] == array[j] and i != j and array[i] not in dictionary:
                #creating a new key-value pair for the local dictionary where the key is the element of the list at index i, and the value is the integer one
                dictionary[array[i]] = 1
                #appending the integer i to a list of indices to make sure that index i is not counted again
                takenIndices.append(i)
            #conditional statement which checks if list values at indices i and j are equivalent, only if i and j are not equal to each other, and if the list element at index i is found in the local dictionary    
            elif array[i] == array[j] and i not in takenIndices and array[i] in dictionary:
                #incrementing an already existing key-value pair by one
                dictionary[array[i]] += 1
                #appending the integer i to a list of indices to make sure that index i is not counted again
                takenIndices.append(i)
        #setting takenIndices list to an empty list for next iteration of i        
        takenIndices = []        

    #conditional statement which checks to make sure that the length of the local dictionary is greater than zero
    if len(dictionary) > 0:
        #for loop which iterates over each value within the local dictionary
        for value in dictionary.values():
            #conditional statement which checks if dictionary's value is greater than maxFrequency
            if value > maxFrequency:
                maxFrequency = value

        #printing out highest frequency information to user        
        print("Highest Frequency Count: " + str(maxFrequency))      
        print("Value(s) that appear " + str(maxFrequency) + " times:", end= " ")  
        #for loop which iterates over each key-value pair in the local dictionary      
        for key, value in dictionary.items():
            #conditional statement which checks if dictionary's value is equal to the maxFrequency
            if value == maxFrequency:
                print(str(key), end= " ")               