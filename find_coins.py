import timeit

# Timing the algorithms for amounts
def time_search_algorithm(algorithm, amount):
    return timeit.timeit(lambda: algorithm(amount), number=1)

# Greedy
def find_coins_greedy(amount):
    denominations = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in denominations:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

# Min
def find_min_coins(amount):
    denominations = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in denominations:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    result = {}
    while amount > 0:
        for coin in denominations:
            if amount >= coin and dp[amount] == dp[amount - coin] + 1:
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                amount -= coin
                break
    return result

# Main
def main():
    amount_to_be_issued = 31173

    coins_greedy = find_coins_greedy(amount_to_be_issued)
    coins_min = find_min_coins(amount_to_be_issued)

    print(f"Homework 9 - find_coins_greedy | The amount to be issued to the client is {amount_to_be_issued} coins with a face value of {coins_greedy}")
    print(f"Homework 9 - find_min_coins | The amount to be issued to the client is {amount_to_be_issued} coins with a face value of {coins_min}")

    print(f"\nHomework 9 | Testing of algorithms...\n")

    for amount in [1000, 10000, 21000, 32000, 43000, 54000, 65000, 76000, 87000, 98000, 109000]:
        find_coins_greedy_time = time_search_algorithm(find_coins_greedy, amount)
        print(f"Homework 9 - find_coins_greedy | For the sum {amount}, the search time was: {find_coins_greedy_time} seconds")

    for amount in [1000, 10000, 21000, 32000, 43000, 54000, 65000, 76000, 87000, 98000, 109000]:
        find_min_coins_time = time_search_algorithm(find_min_coins, amount)
        print(f"Homework 9 - find_min_coins | For the sum {amount}, the search time was: {find_min_coins_time} seconds")


if __name__ == "__main__":
    main()
