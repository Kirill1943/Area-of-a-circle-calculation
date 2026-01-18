import math

print('-' * 30)
print('программа расчета периметра и площади круга: ')
print('-' * 30)


try:
    radius = float(input('введите радиус круга в дециметрах: '))
    perimetr = 2 * math.pi * radius
    ploshad = math.pi * math.pow(radius, 2)

    print('-' * 30)
    print(f'периметр: {perimetr} дециметров')
    print(f'площадь: {ploshad} дециметров')
    print('-' * 30)
except ValueError:
    print('вы вели не число!')
except Exception as e:
    print(f'неожиданная ошибка: {e}')
