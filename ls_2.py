a = input('Введите натуральное число: ')
even = 0
odd = 0

for numeric in a:

    if int(numeric) % 2 == 0:
        even += 1

    else:
        odd += 1

print(f'В данном числе четных цифр: {even}, нечетных цифр: {odd}')