import math
from time import sleep
import sys

def Calculations(n, figura):
    if figura == 'круг':
        n = float(n)
        perimetr = 2 * math.pi * n
        ploshad = math.pi * math.pow(n, 2)
        return [perimetr, ploshad]
    elif figura == 'квадрат':
        n = float(n)
        perimetr = n * 4
        ploshad = n * n
        return [perimetr, ploshad]

print('-' * 30)
print('программа расчета периметра и площади: ')
print('-' * 30)
figura = input('введите площадь и периметр какой фигуры вы хотите расчитать (круг или квадрат): ')
if figura == 'круг':
    radius = input('введите радиус круга в дециметрах: ')
    if not radius.isdigit():
        print('вы ввели не число!')
        print('-' * 30)
        sys.exit(0)
    else:
        radius = float(radius)
        print(f'периметр круга: {Calculations(radius, 'круг')[0]:.3f} дециметров')
        print(f'площадь круга: {Calculations(radius, 'круг')[1]:.3f} дециметров')
        print('-' * 30)
elif figura == 'квадрат':
    radius = input('введите длину стороны квадрата в дециметрах: ')
    if not radius.isdigit():
        print('вы ввели не число!')
        print('-' * 30)
        sys.exit(0)
    else:
        radius = float(radius)
        print(f'периметр квадрата: {Calculations(radius, 'квадрат')[0]:.3f} дециметров')
        print(f'площадь квадрата: {Calculations(radius, 'квадрат')[1]:.3f} дециметров')
        print('-' * 30)

while True:
    sleep(1)
