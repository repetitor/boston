def fib1(k):
    assert k >= 0
    return k if k <= 1 else fib1(k - 1) + fib1(k - 2)


if __name__ == '__main__':
    # n = int(input())
    n = 8
    print(fib1(n))
