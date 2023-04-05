def summa(a, b):
    if a == 0:
        return b
    return summa(a-1, b+1)
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print (summa(a, b))

