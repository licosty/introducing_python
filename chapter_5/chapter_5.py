''' Страница упражнения - 156 '''

# 1
from collections import OrderedDict, defaultdict

import zoo
zoo.hours()

# 2
import zoo as menagerie
menagerie.hours()

# 3
from zoo import hours
hours()

# 4
from zoo import hours as info
info()

# 5
plain = {'a': 1, 'b': 2, 'c': 3}
print(f"\n{plain}")

# 6
print()
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
for key, value in fancy.items():
    print(key, value)

# 7
dict_of_lists = defaultdict(list)
dict_of_lists['a'] = 'something for a'
print(f"\n{dict_of_lists['a']}")