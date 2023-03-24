# O(log n) run time

def binarySearch(list, item):

    low = 0
    high = len(list) - 1

    while(low <= high):
        mid = int((low + high) / 2)  # check middle element
        guess = list[mid]
        if guess == item:  # found item
            return mid
        if guess > item:   # guess too high
            high = mid - 1
        else:              # guess was too low
            low = mid + 1
    return None

my_list = [15, 45, 3, 7, 20]

print(binarySearch(my_list, 7))

