import math

def main():
    def Calculations(n, figura, storon1: float = 1, storon2: int = 1, storon3: int = 1):
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
        elif figura == 'треугольник':
            n = float(n)

            perimetr = storon1 + storon2 + storon3
            polyperimetr = perimetr / 2
            ploshad = math.sqrt(polyperimetr * (polyperimetr - storon1) * (polyperimetr - storon2) * (polyperimetr - storon3))
            
            return [perimetr, ploshad]

    print('-' * 30)
    print('программа расчета периметра и площади: ')
    print('-' * 30)
    figura = input('введите площадь и периметр какой фигуры вы хотите расчитать (круг или квадрат, или треугольник): ')
    if figura == 'круг':
        radius = input('введите радиус круга в дециметрах: ')
        if not radius.isdigit():
            print('вы ввели не число!')
            print('-' * 30)
            return
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
            return
        else:
            radius = float(radius)
            print(f'периметр квадрата: {Calculations(radius, 'квадрат')[0]:.3f} дециметров')
            print(f'площадь квадрата: {Calculations(radius, 'квадрат')[1]:.3f} дециметров')
            print('-' * 30)
    elif figura == 'треугольник':

        s1 = input('1 сторона в дециметрах: ')
        s2 = input('2 сторона в дециметрах: ')
        s3 = input('3 сторона в дециметрах: ')
        if not (s1.isdigit and s2.isdigit and s3.isdigit):
            print('где-то вы ввели не число!')
            print('-' * 30)
            return
        else:
            radius = float(radius)
            print(f'периметр круга: {Calculations(radius, 'круг', storon1=s1, storon2=s2, storon3=s3)[0]:.3f} дециметров')
            print(f'площадь круга: {Calculations(radius, 'круг', storon1=s1, storon2=s2, storon3=s3)[1]:.3f} дециметров')
            print('-' * 30)
