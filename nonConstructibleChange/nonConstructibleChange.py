def nonConstructibleChange(coins):
    coins.sort()

    current = 0

    for coin in coins:
        if coin > current + 1:
            return current + 1

        current += coin

    return current + 1