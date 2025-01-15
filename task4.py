int1 = int(input("Введите число: "))
int2 = int(input("Введите число: "))
int3 = int(input("Введите число: "))

if int1 == int2 and int2 == int3:
    print("3")
elif int1 == int2 and int2 != int3 or int1 == int3 and int3 != int2 or int1 !=int2 and int2 == int3:
    print("2")
else: print("0")
