def sum(num1, num2):
    num1 + num2


sum(10, 5)


class A():
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


# print(D.mro())
