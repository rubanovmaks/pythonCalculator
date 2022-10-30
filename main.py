question = input('Какие числа хотите сложить: ')
if question == 'float':
    value1 = float(input('Введите число: '))
    question2 = input('Какое второе число: ')
    if question2 == 'float':
        value2 = float(input('Введите второе число: '))
elif question == 'int':
    value1 = int(input('Введите первое число: '))
    question2 = input('Какое второе число: ')
    if question2 == 'int':
        value2 = int(input('Введите второе число: '))
else:
    print('error')
    print()
    print('Creating by rubanovmaks')
    quit()
operation = input('Укажите оператор ')
while True:
    if operation == '-':
        result = value1 - value2
        print('Результат:', result)
        print()
        print('Creating by rubanovmaks')
        break
    elif operation == '+':
        result = value1 + value2
        print('Результат:', result)
        print()
        print('Creating by rubanovmaks')
        break
    elif operation == '*':
        result = value1 * value2
        print('Результат:', result)
        print()
        print('Creating by rubanovmaks')
        break
    elif operation == '/':
        result = value1 / value2
        print('Результат:', result)
        print()
        print('Creating by rubanovmaks')
        break
    elif operation == '%':
        result = value1 % value2
        print('Результат:', result)
        print()
        print('Creating by rubanovmaks')
        break
    elif operation == '=':
        result = value1 == value2
        print('Результат:', result)
        print()
        print('Creating by rubanovmaks')
        break
    elif operation == '!=':
        result = value1 != value2
        print('Результат:', result)
        print()
        print('Creating by rubanovmaks')
        break
    else:
        print('error')
        print()
        print('Creating by rubanovmaks')
        break

