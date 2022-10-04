class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, val):
        self.__data = val

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, val):
        if isinstance(val, StackObj) or val is None:
            self.__next = val


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push_back(self, obj):
        if self.last:
            self.last.next = obj

        self.last = obj
        if self.top is None:
            self.top = obj

    def pop_back(self):
        h = self.top
        if h is None:
            return
        while h and h.next != self.last:
            h = h.next
        if h:
            h.next = None
        last = self.last
        self.last = h
        if self.last is None:
            self.top = None
        return last

    def get_data(self):
        res = []
        h = self.top
        while h:
            res.append(h.data)
            h = h.next
        return res

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for i in range(len(other)):
            other[i] = StackObj(other[i])
        for i in other:
            self.push_back(i)
        return self

    def __imul__(self, other):
        for i in range(len(other)):
            other[i] = StackObj(other[i])
        for i in other:
            self.push_back(i)
        return self


# st = Stack()
# st.push_back(StackObj('a1'))
# st.push_back(StackObj('a2'))
# st.push_back(StackObj('a3'))
# print(st.get_data())
# st = st + StackObj('a4')
# print(st.get_data())
# st += StackObj('a5')
# print(st.get_data())
# st = st * ['a6', 'a7']
# print(st.get_data())
# st *= ['a8', 'a9']
# print(st.get_data())

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"



