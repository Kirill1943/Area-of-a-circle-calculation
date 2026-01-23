

def main():
    try:
        from . import периметр_и_площадь, ports
    except ImportError:
        import периметр_и_площадь, ports

    import math, random
    while True:
        primer = input('''
введите операцию
(площадь - вычисление периметра и площади, 
+ = сложение, 
= вычитание, 
* = умножение, 
степень - степени, 
рандом - рандом
e или exit - выход
порты - просматривать статусы портов localhost
ip сайта - просмотреть ip-адрес сайта): 
''')
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
        elif primer == 'рандом':
            min_ = input('минимальное число: ')
            max_ = input('максимальное число: ')

            min_ = min(min_, max_)
            max_ = max(min_, max_)

            print(random.randint(int(min_), int(max_)))
        
        elif primer == 'e' or primer == 'exit':
            print('выход...')
            break
        elif primer == 'порты':
            min__ = int(input('введите минимальный порт: '))
            max__ = int(input('введите максимальный порт: '))
            sleeping = input('скорость ожидания (рекомендуется не сменять) (по умолчанию 0.1): ')
            if sleeping == '':
                pass
            else:
                sleeping = float(sleeping)

            ports.main_scan(min__, max__, sleeping)
        elif primer == 'ip сайта':
            a = input('введите название сайта: ')
            ports.main_dns(a)
        else:
            print(f'операция \'{primer}\' не распознана')


if __name__ == "__main__":
    main()