def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib2(n, mem={}):
    if n == 0 or n == 1:
        return 1
    try:
        return mem[n]
    except KeyError:
        result = fib2(n - 1, mem) + fib2(n - 2, mem)
        mem[n] = result
        return result
