n = int(input('Enter a number: '))
def sum_int(n):
        if n == 0:
            return 0
        else:
            return (sum_int(n - 1)) + n
sum_int(n)
print(sum_int(n))