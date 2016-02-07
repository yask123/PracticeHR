def min_coins(coin_value_list, change, cache):
    minCoins = change

    if change in coin_value_list:
        cache[change] = 1
        return 1
    elif cache[change] > 0:
        return cache[change]
    else:

        for i in [c for c in coin_value_list if c <= change]:
            numCoins = 1 + min_coins(coin_value_list, change - i, cache)

            if numCoins < minCoins:
                minCoins = numCoins
                cache[change] = minCoins
        return minCoins


print min_coins([1, 5, 10, 25], 63, [0] * 64)
