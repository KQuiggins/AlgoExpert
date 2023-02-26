def isValidSubsequence(array, sequence):
    # Initialize two pointers
    arr_index = 0
    seq_index = 0

    # Loop through the array and sequence
    while arr_index < len(array) and seq_index < len(sequence):
        
        # If the array value is equal to the sequence value
        if array[arr_index] == sequence[seq_index]:
            seq_index += 1
        arr_index += 1
    return seq_index == len(sequence) 

# If the sequence index is equal to the length of the sequence, then   the sequence is valid

# O(n) time | O(1) space

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))