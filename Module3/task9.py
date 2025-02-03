from itertools import *

list = ['21', '321', '235']
list = [i for i in permutations(list)]
final_list = [int(''.join(i)) for i in list]
final_list.sort(reverse=True)
print(final_list[0])