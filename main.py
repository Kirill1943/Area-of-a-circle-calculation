import math
from time import sleep
import sys

print('-' * 30)
print('программа расчета периметра и площади круга: ')
print('-' * 30)

radius = input('введите радиус круга в дециметрах: ')

def Calculations(n):
    n = float(n)
    perimetr = 2 * math.pi * n
    ploshad = math.pi * math.pow(n, 2)
    return [perimetr, ploshad]

if not radius.isdigit():
    print('вы ввели не число!')
    print('-' * 30)
    sys.exit(0)
else:
    radius = float(radius)
    print(f'периметр: {Calculations(radius)[0]:.3f} дециметров')
    print(f'площадь: {Calculations(radius)[1]:.3f} дециметров')
    print('-' * 30)


while True:
    sleep(1)
