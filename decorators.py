from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'{t2 - t1}s')
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i*19


long_time()


# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         print('before hello')
#         func(*args, **kwargs)
#         print('after hello')
#     return wrap_func


# @my_decorator
# def hello(greeting, j, e, r, emoji=";0"):
#     print(greeting, j, e, r, emoji)


# hello('whattsupp', '2', '1', '3')
