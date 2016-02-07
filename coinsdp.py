def min_coins(coin_value_list, change):
    minCoins = change

    if change in coin_value_list:
        return 1
    else:

        for i in [c for c in coin_value_list if c <= change]:
            numCoins = 1 + min_coins(coin_value_list, change - i)

            if numCoins < minCoins:
                minCoins = numCoins
        return minCoins


print min_coins([1, 5], 10)
