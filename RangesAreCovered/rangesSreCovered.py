# You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

# Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

# An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.


def is_covered(ranges, left, right):
    covered = [False] * (right - left + 1)  # create a boolean list to keep track of covered integers

    for start, end in ranges:
        for i in range(max(start, left) - left, min(end, right) - left + 1):
            # mark each covered integer as True
            covered[i] = True

    # check if all integers in the range [left, right] are covered
    return all(covered)

ranges = [[1,2],[3,4],[5,6]]
left = 2
right = 5
print(is_covered(ranges, left, right))  # Output: True

