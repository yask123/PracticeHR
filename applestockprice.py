def get_max_stock_price(stock_list):
    min_in_stock_list = stock_list[0]
    max_profit = stock_list[1] - stock_list[0]

    for i in range(1, len(stock_list)):
        current_price = stock_list[i]

        potential_profit = current_price - min_in_stock_list

        max_profit = max(max_profit, potential_profit)

        if current_price < min_in_stock_list:
            min_in_stock_list = current_price

    return max_profit


stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

print get_max_stock_price(stock_prices_yesterday)
