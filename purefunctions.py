from functools import reduce

my_list = [1, 2, 3, 4]
your_list = [10, 20, 30, 40, 50, 50, 50]
my_set = {1, 2, 3, 4, 5, 5, 5}


def multiply_by2(item):
    return item * 2
    # new_list = []
    # for item in li:
    #     new_list.append(item*2)
    # return new_list


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# print(list(map(multiply_by2, my_list)))
odd_list = list(filter(only_odd, my_list))
zip_list = list(zip(my_list, your_list, my_set))
reduced = reduce(accumulator, my_list, 0)
# print(my_list)
# print(new_list)
# print(odd_list)
# print(zip_list)
print(reduced)
# new_list = 12
# print(multiply_by2([1, 2, 3]))

# lambda
print(list(map(lambda item: item*2, my_list)))
print(my_list)
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc+item, my_list))
