def count(coins, n, sum):
    # dp[i] will be storing the number of solutions for
    # value i. We need sum+1 rows as the dp is constructed
    # in bottom up manner using the base case (sum = 0)
    # Initialize all table values as 0
    dp = [0 for k in range(sum + 1)]
    print('starting')
    print(f'{dp}')
    # Base case (If given value is 0)
    dp[0] = 1
    print('Initialized')
    print(f'{dp}')

    # Pick all coins one by one and update the dp[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0, n):
        print('********************************************')
        print(f'i={i} of n={n}')
        for j in range(coins[i], sum + 1):
            print(f'j={j} of {coins[i]} to {sum+1}')
            print(f'dp[{j}]+=dp[{j}-coins[{i}]]')
            dp[j] += dp[j - coins[i]]
            print(f'dp[{j}]={dp[j]} and coins[{i}]={coins[i]}')

        print('End internal loop')
        print(f'{dp}')

    return dp[sum]


# Driver program to test above function
coins = [1, 2, 3]
n = len(coins)
sum = 5
x = count(coins, n, sum)
print(x)
