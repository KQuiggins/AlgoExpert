def findSmallest(arr):

    smallest = arr[0] # Stores the smallest value
    smallest_index = 0 # Stores the index of the smallest value

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr):

    newArr = []

    for i in range(len(arr)):
        smallest = findSmallest(arr) # find smallest element
        newArr.append(arr.pop(smallest)) # adds to newArr

    return newArr

myArr = [16, 7, 3, 9, 32]
print(selection_sort(myArr))
