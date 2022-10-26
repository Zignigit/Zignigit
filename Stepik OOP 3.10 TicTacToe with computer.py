from random import randint

class Cell:
    def __init__(self):
        self.value = 0
        #self.is_free = True

    def __bool__(self):
        return True if self.value == 0 else False


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = [[Cell() for x in range(3)] for y in range(3)]
        self._is_human_win = False
        self._is_computer_win = False
        self._is_draw = False

    @property
    def is_human_win(self):
        return self._is_human_win

    @is_human_win.setter
    def is_human_win(self, val):
        self._is_human_win = val

    def win_check(self):
        res = None
        for i in range(1, 3):
            for row in self.pole:
                if row[0].value == i and row[1].value == i and row[2].value == i:
                    res = i
            for j in range(3):
                if self.pole[0][j].value == i and self.pole[1][j].value == i and self.pole[2][j].value == i:
                    res = i
            if self.pole[0][0].value == i and self.pole[1][1].value == i and self.pole[2][2].value == i:
                res = i
            if self.pole[2][0].value == i and self.pole[1][1].value == i and self.pole[0][2].value == i:
                res = i
        if res == 1:
            self.is_human_win = True
        if res == 2:
            self.is_computer_win = True
        counter = 0
        if counter == 0:
            for i in range(3):
                for j in range(3):
                    if self.pole[i][j].value != 0:
                        counter += 1
        if counter == 9 and self.is_computer_win is False and self.is_human_win is False:
            self.is_draw = True


    @property
    def is_computer_win(self):
        return self._is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, val):
        self._is_computer_win = val

    @property
    def is_draw(self):
        return self._is_draw

    @is_draw.setter
    def is_draw(self, val):
        self._is_draw = val

    def clear(self):
        for row in self.pole:
            for cell in row:
                #cell.is_free = True
                cell.value = 0

    def check_index(self, key):
        if type(key) is tuple:
            if type(key[0]) is not int or type(key[1]) is not int or key[0] < 0 or key[1] < 0 or key[0] > 2 or key[1] > 2:
                raise IndexError('некорректно указанные индексы')
        if type(key) is int:
            if key < 0 or key > 2:
                raise IndexError('некорректно указанные индексы')
        if type(key) not in (int, tuple):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.check_index(item)
        if 'slice' not in str(item):
            return self.pole[item[0]][item[1]].value
        if type(item) is tuple:
            if type(item[0]) is int:
                return tuple([self.pole[item[0]][0].value, self.pole[item[0]][1].value, self.pole[item[0]][2].value])
            if type(item[1]) is int:
                n = item[1]
                return tuple([self.pole[0][n].value, self.pole[1][n].value, self.pole[2][n].value])

    def __setitem__(self, key, value):
        self.check_index(key)
        if not self.pole[key[0]][key[1]].value == 0:
            raise ValueError('клетка уже занята')
        self.pole[key[0]][key[1]].value = value
        self.win_check()
        #self.pole[key[0]][key[1]].is_free = False

    def show(self):
        for row in self.pole:
            for i in row:
                print(i.value, end=' ')
            print()
        print('_____________')

    def free_cells(self):
        res = []
        for i in range(len(self.pole)):
            for j in range(len(self.pole[i])):
                if self.pole[i][j].value == 0:
                    res.append([i, j])
        return res

    def human_go(self):
        b = input('ходи:')
        a = tuple(map(int, b.split(' ')))
        self.check_index(a)
        if list(a) not in self.free_cells():
            print('занято')
            self.human_go()
        else:
            self.pole[a[0]][a[1]].value = 1
            #self.pole[a[0]][a[1]].is_free = False
        self.win_check()

    def computer_go(self):
        lst = self.free_cells()
        a = lst[randint(0, len(lst))-1]
        self.pole[a[0]][a[1]].value = 2
        #self.pole[a[0]][a[1]].is_free = False
        self.win_check()

    def __bool__(self):
        if self.is_draw or self.is_human_win or self.is_computer_win:
            return False
        return True

    def init(self):
        self.clear()
        self.is_draw = False
        self.is_human_win = False
        self.is_computer_win = False
        self.pole = [[Cell() for x in range(3)] for y in range(3)]






# t = TicTacToe()
# t.show()
# t[0, 0] = 2
# t[0, 1] = 2
# t[0, 2] = 1
# t[1, 0] = 1
# t[1, 1] = 1
# t[1, 2] = 2
# t[2, 0] = 2
# t[2, 1] = 1
# t[2, 2] = 1
# t.show()
# print(t.is_draw)
# t.win_check()
# print(t.is_draw)


# game = TicTacToe()
# game.init()
# step_game = 0
# print(bool(game))
# while game:
#     game.show()
#
#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()
#
#     step_game += 1
#
#
# game.show()
#
# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
game.show()
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"