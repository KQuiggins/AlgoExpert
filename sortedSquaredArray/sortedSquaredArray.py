def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    
    smallerValueIndex = 0  # first 
    largerValueIndex = len(array) - 1  # last

    # Loop in reverse to be able to build array from right to left
    for index in reversed(range(len(array))):

        smallerValue = array[smallerValueIndex]
        largerValue = array[largerValueIndex]

        if abs(smallerValue) > abs(largerValue): # get absolute value 
            sortedSquares[index] = smallerValue * smallerValue
            smallerValueIndex += 1
        else:
            sortedSquares[index] = largerValue * largerValue
            largerValueIndex -= 1

    return sortedSquares