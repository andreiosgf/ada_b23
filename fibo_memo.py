def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result
    return result


if __name__ == '__main__':
    for x in range(0,9):
        y = fibonacci(x)
        print(y)
