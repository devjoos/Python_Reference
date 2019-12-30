fib_cache = {}


def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]

    if n == 0:
        value = 0
    # First Fibonacci number is 0
    elif n == 1 or n == 2:
        # print(f'this is how many times 1 or 2 gets called {n}')
        value = 1
    else:
        # print(f'this is the recursion number:{n}')
        value = fibonacci(n-1) + fibonacci(n-2)
    fib_cache[n] = value
    return value


# print(fibonacci(1000))


def fib(n):
    a = 1
    b = 1
    for _ in range(n):
        yield a
        temp = a
        a = b
        b = temp + b


fib(5)

x = y = z = "oranage"
print(x)
print(y)
print(z)


# for n in range(1, 50):
#     print(f'{n}: {Fibonacci(n)}')


def fibonacci_loop(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    elif num > 2:
        a = 1  # variable for (n - 1)
        b = 1  # variable for (n - 2)
        for _ in range(3, num + 1):
            c = a + b  # 2
            a = b
            b = c
            # a, b = b, c
            print(c)

        return c


# (fibonacci_loop(3))


# def fibonacci_recursion(num):
#     '''Return a fibonacci sequence value of num'''
#     if num == 0:
#         return 0
#     if num == 1 or num == 2:
#         return 1
#     # print(num)
#     return fibonacci_recursion(num - 2) + fibonacci_recursion(num - 1)
