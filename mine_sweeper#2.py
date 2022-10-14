from random import randint

# сапер со степика https://stepik.org/lesson/701992/step/9?unit=702093, этот рабочий с дескрипторами, на сайте принимает только проперти

class Descr__:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.name in ('__is_mine', '__is_open') and type(value) is not bool:
            raise ValueError("недопустимое значение атрибута")
        if self.name in ('__number') and value < 0 or value > 8:
            raise ValueError("недопустимое значение атрибута")
        instance.__dict__[self.name] = value


class Cell:
    is_mine = Descr__()
    number = Descr__()
    is_open = Descr__()

    def __init__(self, is_mine=False, number=0, is_open=False):
        if type(is_mine) is bool and type(is_open) is bool and type(number) is int:
            self.is_mine = is_mine
            self.number = number
            self.is_open = is_open
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        return not bool(self.is_open)

    def __repr__(self):
        return str('#') if self.is_open is False else ('*') if self.is_mine is True else str(self.number)


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, n, m, total_mines):
        self.N = n
        self.M = m
        self.total_mines = total_mines
        self.__pole_cells = []

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        for i in range(self.N):
            self.__pole_cells.append([Cell() for j in range(self.M)])
        mines = []
        indxs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        while len(mines) < self.total_mines:
            a = randint(0, self.N-1)
            b = randint(0, self.M-1)
            if [a, b] not in mines:
                mines.append([a, b])
        for i in mines:
            self.__pole_cells[i[0]][i[1]].is_mine = True
            for j in indxs:
                try:
                    c = i[0] + j[0]
                    d = i[1] + j[1]
                    if 0 <= c <= self.N and 0 <= d <= self.M:
                        self.__pole_cells[c][d].number += 1
                except:
                    continue


    def open_cell(self, i, j):
        if i < self.N and j < self.M:
            self.__pole_cells[i][j].is_open = True
        else:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self):
        for i in self.__pole_cells:
            for j in i:
                print(j, end=' ')
            print()

    # def __repr__(self):
    #     res = []
    #     for i in self.__pole_cells:
    #         res.append([j for j in i])
    #     return str(res)



gp = GamePole(10, 20, 20)
gp.init_pole()
gp.open_cell(4, 2)
gp.open_cell(1, 2)
gp.open_cell(0, 2)
gp.show_pole()

