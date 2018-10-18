# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Figure:
    """Документация for Figure"""

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def move(figure, point):
        figure.x1 = point.x1
        figure.y1 = point.y1
        figure.x2 = point.x2
        figure.y2 = point.y2

    def square(self):
        pass
        print('У абстрактной фигуры нет площади')


class Triangle(Figure):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__(x1, y1, x2, y2)
        self.x3 = x3
        self.y3 = y3
        # стороны:
        self.a = math.sqrt(((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2))
        self.b = math.sqrt(((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2))
        self.c = math.sqrt(((self.x3 - self.x1)**2 + (self.y3 - self.y1)**2))

    @property
    def area(self):
        p = 0.5*(self.a + self.b + self.c)
        S = math.sqrt((p*(p - self.a)*(p - self.b)*(p - self.c)))
        return "Площадь треугольника abc равна: S = {} усл. ед. в кв.\n".format(round(S, 3))

    @property
    def perim(self):
        return "Периметр треугольника abc равен: Per = {} усл. ед.\n".format(round((self.a + self.b + self.c), 3))

    @property
    def heigth(self):
        p = 0.5*(self.a + self.b + self.c)
        S = math.sqrt((p*(p - self.a)*(p - self.b)*(p - self.c)))
        return "Высота треугольника abc к стороне 'a' равна: H = {} усл. ед.\n" \
               "Высота треугольника abc к стороне 'b' равна: H = {} усл. ед.\n" \
               "Высота треугольника abc к стороне 'c' равна: H = {} усл. ед.\n" \
            .format(round(S*2/self.a, 3), round(S*2/self.b, 3), round(S*2/self.c, 3))

    def __str__(self):
        return "Треугольник abc со сторонами: a = {}, b = {}, c = {} усл. ед.\n"\
            .format(round(self.a, 3), round(self.b, 3), round(self.c, 3))


tri = Triangle(2, 2, 4, 6, 6, 3)
tri_P = Triangle(2, 2, 4, 6, 6, 3).perim
tri_S = Triangle(2, 2, 4, 6, 6, 3).area
tri_H = Triangle(2, 2, 4, 6, 6, 3).heigth
print(tri, tri_P, tri_S, tri_H)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
import math


class Figure:
    """Документация for Figure"""

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def move(figure, point):
        figure.x1 = point.x1
        figure.y1 = point.y1
        figure.x2 = point.x2
        figure.y2 = point.y2

    def square(self):
        pass
        print('У абстрактной фигуры нет площади')


class Trapeze(Figure):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2)
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        # стороны:
        self.a = math.sqrt(((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2))
        self.b = math.sqrt(((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2))
        self.c = math.sqrt(((self.x4 - self.x3)**2 + (self.y4 - self.y3)**2))
        self.d = math.sqrt(((self.x4 - self.x1)**2 + (self.y4 - self.y1)**2))
        # высота (формула из учебника):
        self.h = math.sqrt(self.a**2 - ((((self.d - self.b)**2) + self.a**2 - self.c**2)/(2*(self.d - self.b)))**2)
        # диагонали:
        self.d1 = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)
        self.d2 = math.sqrt((self.x4 - self.x2) ** 2 + (self.y4 - self.y2) ** 2)

    @property
    def test_trap(self):
        if self.a == self.c:
            res = 'является равнобедренной трапецией'
        # свойство:
        elif self.d1 ** 2 + self.d2 ** 2 != 2 * self.b * self.d + self.a ** 2 + self.c ** 2:
            res = 'не является трапецией'
        elif self.a != self.c:
            res = 'не является равнобедренной трапецией'
        else:
            res = 'не является трапецией'
        return "Фигура abcd: {}\n".format(res)

    @property
    def heigth(self):
        return "Высота трапеции abcd равна: H = {} усл. ед.\n".format(round(self.h, 3))

    @property
    def area(self):
        S = 0.5*(self.b + self.d)*self.h
        return "Площадь трапеции abcd равна: S = {} усл. ед. в кв.\n".format(round(S, 3))

    @property
    def perim(self):
        return "Периметр трапеции abcd равен: Per = {} усл. ед.\n".format(round((self.a + self.b + self.c + self.d), 3))

    def __str__(self):
        return "Трапеция abcd со сторонами: a = {}, b = {}, c = {}, d = {} усл. ед.\n"\
            .format(round(self.a, 3), round(self.b, 3), round(self.c, 3), round(self.d, 3))

tra = Trapeze(2, 8, 3, 12, 6, 14, 10, 13)
tra_T = Trapeze(2, 8, 3, 12, 6, 14, 10, 13).test_trap
tra_P = Trapeze(2, 8, 3, 12, 6, 14, 10, 13).perim
tra_S = Trapeze(2, 8, 3, 12, 6, 14, 10, 13).area
tra_H = Trapeze(2, 8, 3, 12, 6, 14, 10, 13).heigth
# пример не трапеции - 2, 2, 3, 6, 8, 6, 9, 0
# равнобедренная трапеция - 2, 8, 3, 12, 6, 14, 10, 13
# просто трапеция - 0, 8, 3, 12, 6, 14, 10, 13
print(tra, tra_T, tra_P, tra_S, tra_H)
