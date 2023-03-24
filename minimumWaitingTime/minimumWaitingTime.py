def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    totalWaitingTime = 0
    for i in range(len(queries)):
        duration = queries[i]
        queriesLeft = len(queries) - (i + 1)
        totalWaitingTime += duration * queriesLeft
        print(totalWaitingTime,  duration, queriesLeft )
    return totalWaitingTime

queries = [3, 2, 1, 2, 6]
print(minimumWaitingTime(queries))