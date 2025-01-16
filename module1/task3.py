integer1 = input("Введите число: ")
integer2 = input("Введите число: ")

if "." in integer1:                  #для красоты конвертируем целые числа в int, а дробные во float
    integer1 = float(integer1)
else: integer1 = int(integer1)

if "." in integer2:
    integer2 = float(integer2)
else: integer2 = int(integer2)

if integer1 > integer2:
    print(integer1)
else: print(integer2)