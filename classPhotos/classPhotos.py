def classPhotos(redShirtHeights, blueShirtHeights):
    # reverse sort the arrays so that the tallest person is at the front
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    # Determine which shirt color is in the first row
    firstRowShirtColor = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"

    for idx in range(len(redShirtHeights)):
        # Get the heights of the current student
        redShirtHeight = redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]

        # If the first row is red, then the red shirt student must be taller than the blue shirt student
        if firstRowShirtColor == "RED":
            if redShirtHeight >= blueShirtHeight:
                return False
        # If the first row is blue, then the blue shirt student must be taller than the red shirt student
        else:
            if blueShirtHeight >= redShirtHeight:
                return False
    # If we make it here, then all students are in the correct row        
    return True
    
redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights = [6, 9, 2, 4, 5]
print(classPhotos(redShirtHeights, blueShirtHeights))

# Output: True

# Time: O(nlog(n)) | Space: O(1)

# The time complexity of this code is O(nlogn) because of the two sorting operations that are performed on the input lists of heights. The sort() function used on both redShirtHeights and blueShirtHeights sorts the lists in place using a comparison-based sorting algorithm, such as quicksort or mergesort, both of which have an average time complexity of O(nlogn).

# The two lists have a combined length of 2n, so the sorting operation will take O(2nlog(2n)) time, which simplifies to O(nlogn) time. This is the dominant factor in the time complexity of the classPhotos function, as the subsequent loop over the sorted lists has a time complexity of O(n).

# Therefore, the overall time complexity of the classPhotos function is O(nlogn) due to the two sorting operations on the input lists.


    