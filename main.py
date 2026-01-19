import периметр_и_площадь
import math

while True:
    primer = input('введите операцию (площадь - вычисление периметра и площади, + = сложение, - = вычитание, * = умножение): ')
    if primer == 'площадь':
        периметр_и_площадь.main()
    elif primer == '+':
        int1 = float(input('введите 1 число: '))
        int2 = float(input('введите 2 число: '))

        print(f'сумма: {int1 + int2}')
    elif primer == '-':
        int1 = float(input('введите 1 число: '))
        int2 = float(input('введите 2 число: '))

        print(f'разность: {int1 - int2}')
    elif primer == '*':
        int1 = float(input('введите 1 число: '))
        int2 = float(input('введите 2 число: '))

        print(f'произведение: {int1 * int2}')
    elif primer == '/':
        int1 = float(input('введите 1 число (не 0!): '))
        int2 = float(input('введите 2 число (не 0!): '))

        if int2 == 0.0:
            print('деление на ноль!')
        else:
            print(f'частное: {int1 / int2}')
    elif primer == 'степень':
        int1 = float(input('1 число: '))
        int2 = float(input('2 число: '))

        print(f'степень чисел: {math.pow(int1, int2)}')
    else:
        print(f'операция {primer} не распознана')
