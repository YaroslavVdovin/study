from random import randint
n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]
full_list = [i for k in m for i in k]
full_list.sort()
print(full_list[-1])