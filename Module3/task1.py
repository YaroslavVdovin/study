x = int(input("Размер вклада: "))
y = int(input("Целевая сумма: "))
p = int(input("Процентная ставка: "))
years = 0

while x < y:
      x += round((x // 100 * p), 0)
      years += 1
print(years)