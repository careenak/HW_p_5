def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        return a / b


def is_correct_operator(operator):
    return operator == '0' or operator == '+' or operator == '-' or operator == '*' or operator == '/'


def get_operator():
    return input('Введите операцию (+, -, *, / или 0 для выхода): ')


def run_calculator(a=None, b=None):
    if a is None:
        a = float(input('Введите первое число: '))
    if b is None:
        b = float(input('Введите второе число: '))
    operator = get_operator()

    if not is_correct_operator(operator):
        print('Ввели некорректную операцию')
        run_calculator(a, b)
        return
    elif operator == '0':
        return
    elif operator == '/' and b == 0:
        print('Не могу делить на 0')
        run_calculator()
        return
    else:
        print(calculate(a, b, operator))
        run_calculator()


run_calculator()