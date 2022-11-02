import math


class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, val):
        self._dist = val

    def __eq__(self, other):
        return hash((self.v1, self.v2)) in (hash((other.v1, other.v2)), hash((other.v2, other.v1)))


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if not isinstance(v, Vertex):
            raise TypeError('не вертекс!')
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if not isinstance(link, Link):
            raise TypeError('не линк!')
        if link not in self._links:
            self._links.append(link)
        if link.v2 not in self._vertex:
            self.add_vertex(link.v2)
        if link.v1 not in self._vertex:
            self.add_vertex(link.v1)
        if link not in link.v1._links:
            link.v1._links.append(link)
        if link not in link.v2._links:
            link.v2._links.append(link)

    def find_path(self, start_v, stop_v):
        D = [[math.inf for vertex in self._vertex] for vertex in self._vertex]     # создаю пустую смежную матрицу по количеству вершин
        for link in self._links:                                            # заполняю матрицу
            j = self._vertex.index(link._v2)
            i = self._vertex.index(link._v1)
            D[i][j] = link._dist
            D[j][i] = link._dist

        def arg_min(T, S):
            amin = -1
            m = math.inf  # максимальное значение
            for i, t in enumerate(T):
                if t < m and i not in S:
                    m = t
                    amin = i

            return amin

        def get_link(v, D):
            for i, w in enumerate(D[v]):
                if w > 0:
                    yield i

        N = len(D)  # число вершин в графе
        T = [math.inf] * N  # последняя строка таблицы

        v = self._vertex.index(stop_v)  # стартовая вершина (нумерация с нуля)
        S = {v}  # просмотренные вершины
        T[v] = 0  # нулевой вес для стартовой вершины
        M = [0] * N  # оптимальные связи между вершинами

        while v != -1:  # цикл, пока не просмотрим все вершины
            for j in get_link(v, D):  # если вершина еще не просмотрена
                if j not in S:  # перебираем все связанные вершины с вершиной v
                    w = T[v] + D[v][j]
                    if w < T[j]:
                        T[j] = w
                        M[j] = v  # связываем вершину j с вершиной v

            v = arg_min(T, S)  # выбираем следующий узел с наименьшим весом
            if v >= 0:  # выбрана очередная вершина
                S.add(v)  # добавляем новую вершину в рассмотрение
        # формирование оптимального маршрута:
        end = self._vertex.index(start_v)
        start = self._vertex.index(stop_v)
        P = [end]
        counter = 0
        while end != start:
            counter += 1
            end = M[P[-1]]
            P.append(end)
        vertex_lst = []
        links_lst = []
        for vertex_index in P:
            vertex_lst.append(self._vertex[vertex_index])
        for lnk in self._links:
            for i in range(1, len(vertex_lst)):
                if hash((vertex_lst[i], vertex_lst[i-1])) in (hash((lnk.v1, lnk.v2)), hash((lnk.v2, lnk.v1))):
                    links_lst.append(lnk)


        return vertex_lst, links_lst


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self._dist = dist

# map_graph = LinkedGraph()
#
# v1 = Vertex()
# v2 = Vertex()
# v3 = Vertex()
# v4 = Vertex()
# v5 = Vertex()
# v6 = Vertex()
# v7 = Vertex()
#
# map_graph.add_link(Link(v1, v2))
# map_graph.add_link(Link(v2, v3))
# map_graph.add_link(Link(v1, v3))
# map_graph.add_link(Link(v4, v5))
# map_graph.add_link(Link(v6, v7))
# map_graph.add_link(Link(v2, v7))
# map_graph.add_link(Link(v3, v4))
# map_graph.add_link(Link(v5, v6))
#
# print(len(map_graph._links))   # 8 связей
# print(len(map_graph._vertex))  # 7 вершин
#
#
# # for i, vertex in enumerate(map_graph._vertex):
# #     if vertex == v1:
# #         print(f'v1 - {i}')
# #     if vertex == v2:
# #         print(f'v2 - {i}')
# #     if vertex == v3:
# #         print(f'v3 - {i}')
# #     if vertex == v4:
# #         print(f'v4 - {i}')
# #     if vertex == v5:
# #         print(f'v5 - {i}')
# #     if vertex == v6:
# #         print(f'v6 - {i}')
# #     if vertex == v7:
# #         print(f'v7 - {i}')
# path = map_graph.find_path(v1, v6)
#
# print(path)


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

#print(len(map_metro._links))
#print(len(map_metro._vertex))
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]

print(sum([x.dist for x in path[1]]))  # 7



map2 = LinkedGraph()
v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()

map2.add_link(Link(v1, v2))
map2.add_link(Link(v2, v3))
map2.add_link(Link(v2, v4))
map2.add_link(Link(v3, v4))
map2.add_link(Link(v4, v5))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

map2.add_link(Link(v2, v1))
assert len(map2._links) == 5, "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"

path = map2.find_path(v1, v5)
s = sum([x.dist for x in path[1]])
assert s == 3, "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"

assert issubclass(Station, Vertex) and issubclass(LinkMetro, Link), "класс Station должен наследоваться от класса Vertex, а класс LinkMetro от класса Link"

map2 = LinkedGraph()
v1 = Station("1")
v2 = Station("2")
v3 = Station("3")
v4 = Station("4")
v5 = Station("5")

map2.add_link(LinkMetro(v1, v2, 1))
map2.add_link(LinkMetro(v2, v3, 2))
map2.add_link(LinkMetro(v2, v4, 7))
map2.add_link(LinkMetro(v3, v4, 3))
map2.add_link(LinkMetro(v4, v5, 1))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"

path = map2.find_path(v1, v5)

assert str(path[0]) == '[1, 2, 3, 4, 5]', path[0]
s = sum([x.dist for x in path[1]])
assert s == 7, "неверная суммарная длина маршрута для карты метро"