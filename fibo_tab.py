def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        table = [0] * (n + 1)
        table[0] = 0
        table[1] = 1
        for i in range(2, n + 1):
            table[i] = table[i - 1] + table[i - 2]
        return table[n]


if __name__ == '__main__':
    table2=[0]*(11)
    print(table2)

    for x in range(0, 9):
        y = fibonacci(x)
        print(y)
