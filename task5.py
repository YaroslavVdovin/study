x1 = int(input("Введите номер строки 1: "))
y1 = int(input("Введите номер столбца 1: "))
x2 = int(input("Введите номер строки 2: "))
y2 = int(input("Введите номер столбца 2: "))

if abs(x1 - x2) <= 7 and y1 == y2 or x1 == x2 and abs(y1 - y2) <= 7:
    print("YES")
else: print("NO")