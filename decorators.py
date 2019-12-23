def my_decorator(func):
    def wrap_func(x):
        print('before hello')
        func(x)
        print('after hello')
    return wrap_func


@my_decorator
def hello(greeting):
    print(greeting)


hello('whattsupp')
