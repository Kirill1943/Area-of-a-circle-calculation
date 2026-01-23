
import math

def Calculations(figura, a=0, b=0, c=0):
    if figura == 'круг':
        perimetr = 2 * math.pi * a
        ploshad = math.pi * (a ** 2)
        return perimetr, ploshad
    elif figura == 'квадрат':
        perimetr = a * 4
        ploshad = a * a
        return perimetr, ploshad
    elif figura == 'треугольник':
        perimetr = a + b + c
        p = perimetr / 2
        # Формула Герона
        ploshad = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return perimetr, ploshad
    elif figura == 'прямоугольник':
        perimetr = (a + b) * 2
        ploshad = a * b

        return perimetr, ploshad

def main():
    print('-' * 30)
    print('Программа расчета периметра и площади:')
    print('-' * 30)
    figura = input('Введите фигуру (круг, квадрат, треугольник, прямоугольник): ').lower()

    try:
        if figura == 'круг':
            r = float(input('Введите радиус (дм): '))
            p, s = Calculations('круг', a=r)
            print(f'Периметр: {p:.3f} дм\nПлощадь: {s:.3f} дм²')

        elif figura == 'квадрат':
            a = float(input('Введите сторону (дм): '))
            p, s = Calculations('квадрат', a=a)
            print(f'Периметр: {p:.3f} дм\nПлощадь: {s:.3f} дм²')

        elif figura == 'треугольник':
            s1 = float(input('1-я сторона: '))
            s2 = float(input('2-я сторона: '))
            s3 = float(input('3-я сторона: '))
            
            # Проверка существования треугольника
            if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
                p, s = Calculations('треугольник', a=s1, b=s2, c=s3)
                print(f'Периметр: {p:.3f} дм\nПлощадь: {s:.3f} дм²')
            else:
                print("Треугольник с такими сторонами не существует!")
        elif figura == 'прямоугольник':
            s1 = float(input('1 сторона: '))
            s2 = float(input('2 сторона: '))

            print(f'Периметр: дм {Calculations('прямоугольник', a=s1, b=s2)[0]:.3f}\nплощадь: {Calculations('прямоугольник', a=s1, b=s2)[1]:.3f} дм²')

        else:
            print("Неизвестная фигура")
    except ValueError:
        print("Ошибка: введите числовое значение!")
    
    print('-' * 30)

if __name__ == '__main__':
    main()