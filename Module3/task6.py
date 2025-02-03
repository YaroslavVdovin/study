dict1 = {'test':5, 'test2':3}
dict_buff = {}
for i in dict1.keys():
    tempkey = i
    tempvalue = dict1.get(tempkey)
    dict_buff.update({tempvalue:tempkey})
dict1 = dict_buff
print(dict1)