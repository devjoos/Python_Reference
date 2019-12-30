# essentially this is what a for loop is doing behind the scenes
def special_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


# this mimics what a range does
class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen:
    print(i)


# special_for_loop([1, 2, 3, 4])


# def generator_function(num):
#     for i in range(num):
#         yield i


# g = generator_function(100)
# print(next(g))
# next(g)
# next(g)
# print(next(g))


# # since generators are iterables you can loop through them
# # for item in generator_function(10000):
# #     print(item)
