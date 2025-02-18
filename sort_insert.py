array = [9, 32, 5, 43, 1, 235]
def insert_sort(array):
    for i in range(len(array)):
        target = array[i]
        j = i - 1
        while array[j] > target and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = target
    return array
print(insert_sort(array))