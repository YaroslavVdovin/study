v = int(input("Введите скорость: "))
t = int(input("Введите время: "))
length = t * v
lengthconst = 109
if length <= lengthconst:
    print(length)
elif length > lengthconst and length / lengthconst < 2:        #МКАД кольцо - тут мы проверяем, проехал ли мотоциклист больше одного кольца
    length -= lengthconst
    print(length)
else:
    circles = length // lengthconst                             #тут мы узнаем, сколько кругов по МКАДУ проехал мотоциклист и смотрим, на каком км он остановился
    length -= (circles * lengthconst)
    print(length)