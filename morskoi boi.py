from random import randint

class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1 for i in range(self._length)]
        self.coords = []
        self.occupied = []

    def set_coords_and_occupied(self):
        self.coords = []
        self.occupied = []
        for i in range(self._length):
            if self._tp == 1:
                self.coords.append((self._x + i, self._y))
            if self._tp == 2:
                self.coords.append((self._x, self._y + i))
        nearbys = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for coord in self.coords:
            for near in nearbys:
                self.occupied.append((coord[0] + near[0], coord[1] + near[1]))
        self.occupied = list(set(self.occupied + self.coords))


    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return (self._x, self._y)

    def move(self, go):
        if self._is_move:
            if self._tp == 1:
                self._x += go
            if self._tp == 2:
                self._y += go

    def is_collide(self, ship):
        self.set_coords_and_occupied()
        ship.set_coords_and_occupied()
        for coord in self.coords:
            if coord in ship.occupied:
                return True
        return False

    def is_out_pole(self, size):
        self.set_coords_and_occupied()
        for coord in self.coords:
            if size - 1 < coord[0] or coord[1] > size - 1 or coord[0] < 0 or coord[1] < 0:
                return True
        return False

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []
        self._pole = None
        self.init()

    def init(self):
        self._ships = []
        ships = [4, 3, 3, 2, 2, 2, 1, 1, 1 ,1]
        for i in ships:
            ship = Ship(i, tp=randint(1, 2))
            while ship not in self._ships:
                ship.set_start_coords(randint(0, self._size - 1), randint(0, self._size - 1))
                ship.set_coords_and_occupied()

                res = True
                if ship.is_out_pole(self._size):
                    res = False
                if self._ships:
                    for s in self._ships:
                        if s != ship and ship.is_collide(s):
                            res = False
                if res:
                    self._ships.append(ship)

                # if not ship.is_out_pole(self._size) and self.ship_collision() is False:
                #     self._ships.append(ship)

    def ship_collision(self):
        if self._ships:
            for s in self._ships:
                if s.is_out_pole(self._size):
                    return True
                for sh in self._ships:
                    if s != sh and sh.is_collide(s):
                        # print('collision', s.coords, sh.coords)
                        return True
        return False

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            ship.move(1)
            if self.ship_collision():
                ship.move(-2)
            if self.ship_collision():
                ship.move(1)

    def show(self):
        for i in self.get_pole():
            print(*i)
        print()

    def get_pole(self):
        self._pole = [[0 for i in range(self._size)] for j in range(self._size)]
        for ship in self._ships:
            for j in range(len(ship.coords)):
                self._pole[ship.coords[j][0]][ship.coords[j][1]] = ship._cells[j]
        res = []
        for i in self._pole:
            res.append(tuple(i))
        return tuple(res)


# g = GamePole(8)
# g.show()
# g.move_ships()
# g.show()

ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)

assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"

ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)

assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(
    s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"

p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"

        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()

gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"

pole_size_8 = GamePole(8)
pole_size_8.init()

