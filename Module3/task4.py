i = [1, 4, 1, 6, "hello", "a", 5, "hello"]
doubles = [val for j, val in enumerate(i) if val in i[j+1:]]
print(doubles)