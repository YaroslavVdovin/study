array = [2, 5, 4, 10, 3, 1, 7]
array.sort()
nuzhno_naiti = int(input('Какое число найти: '))
def binary_search(array, nuzhno_naiti):
        centre = len(array) // 2 #находим центр массива
        if array[centre] != nuzhno_naiti: #если центр не то, что нужно, мы делим список на два подсписка, исключая центр
            left = array[:centre]
            right = array[centre + 1:]
            if nuzhno_naiti < array[centre]: #если искомое число меньше центрового, мы ищем в массиве меньше центра
                 if len(left) < 1: #базовый случай - массив закончился
                   return 'Такого нет'
                 else:
                    return binary_search(left, nuzhno_naiti) #рекурсивно бъём разбитый меньший массив еще на два, возвращаемся в начало функции
            elif nuzhno_naiti > array[centre]: #если искомое число больше центрового, мы ищем в массиве больше центра
                 if len(right) < 1: #базовый случай - массив закончился
                    return 'Такого нет'
                 else:
                    return binary_search(right, nuzhno_naiti) #рекурсивно бъём разбитый больший массив еще на два, возвращаемся в начало функции
        else:
            return 'Такое число есть'
print(binary_search(array, nuzhno_naiti))