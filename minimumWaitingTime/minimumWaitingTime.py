def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    totalWaitingTime = 0
    for i in range(len(queries)):
        duration = queries[i]
        queriesLeft = len(queries) - (i + 1)
        totalWaitingTime += duration * queriesLeft
    return totalWaitingTime