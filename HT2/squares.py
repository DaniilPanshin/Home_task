import math


def circle_area(r):
    return math.pi * (r ** 2)


def polygon_area(n, a):
    return n * (a ** 2) / (4 * math.tan(math.pi / n))


def triangle_area(sides):
    p = 0
    if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]:
        for i in sides:
            p += i
        p = p / 2
        return (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5
    else:
        print("Треугольник не существует")


def rect_area(sides):
    return sides[0] * sides[1]


def trapez_area(sides):
    return (sides[0] + sides[1]) * sides[2] / 2


print('Выберите, площадь какой фигуры, вы хотите найти:'
      '\n1 - круг\n2 - правильный многоугольник\n3 - треугольник\n4 - прямоугольник\n5 - трапеция')
figure = int(input())
if figure == 1:
    print('Введите радиус круга:')
    r = int(input())
    print('Площадь круга =', circle_area(r))
elif figure == 2:
    print('Введите количество сторон многоугольника:')
    n = int(input())
    print('Введите длину стороны многоугольника:')
    a = int(input())
    print('Площадь правильного многоугольника =', polygon_area(n, a))
elif figure == 3:
    print('Введите длины сторон треугольника:')
    sides = [int(i) for i in input().split()]
    if len(sides) != 3:
        print('Вы ввели неверное количество чисел')
    else:
        print('Площадь треугольника =', triangle_area(sides))
elif figure == 4:
    print('Введите длину и ширину прямоугольника:')
    sides = [int(i) for i in input().split()]
    if len(sides) != 2:
        print('Вы ввели неверное количество чисел')
    else:
        print('Площадь прямоугольника =', rect_area(sides))
elif figure == 5:
    print('Введите длины оснований трапеции и ее высоту:')
    sides = [int(i) for i in input().split()]
    if len(sides) != 3:
        print('Вы ввели неверное количество чисел')
    else:
        print('Площадь трапеции =', trapez_area(sides))
else:
    print('Этой фигуры нет в списке')
