from collections import Counter, OrderedDict, defaultdict
import datetime

print(datetime.date.today())

my_list = [1, 2, 3, 4, 5, 6, 7, 7, 7]

print(Counter(my_list))

my_dict = defaultdict(lambda: 4, {'a': 1, 'b': 2})

print(my_dict['c'])

a = OrderedDict()
a['a'] = 1
a['b'] = 2

a2 = OrderedDict()
a2['a'] = 1
a2['b'] = 2
