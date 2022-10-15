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

    def __str__(self):
        return str(self.__data)


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.last:
            self.last.next = obj

        self.last = obj
        if self.top is None:
            self.top = obj

    def pop(self):
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
        self.push(other)
        return self

    def __iadd__(self, other):
        self.push(other)
        return self

    def __mul__(self, other):
        for i in range(len(other)):
            other[i] = StackObj(other[i])
        for i in other:
            self.push(i)
        return self

    def __imul__(self, other):
        for i in range(len(other)):
            other[i] = StackObj(other[i])
        for i in other:
            self.push(i)
        return self

    def __len__(self):
        counter_max = 0
        maxnext = self.top
        while maxnext.next:
            counter_max += 1
            maxnext = maxnext.next
        return counter_max + 1

    def __getitem__(self, item):
        if type(item) is not int or item < 0 or item > len(self)-1:
            raise IndexError('неверный индекс')
        a = 0
        res = self.top
        while a != item:
            res = res.next
            a += 1
        return res

    def __setitem__(self, key, value):
        if type(key) is not int or key < 0 or key > len(self)-1:
            raise IndexError('неверный индекс')

        # if key = 0
        if key == 0:
            next_next = self.top.next
            self.top = value
            self.top.next = next_next

        counter = 0
        res = self.top
        # if key > 0, not last(?)
        while counter != key:
            if counter + 1 == key:
                next_next = res.next.next
                res.next = value
                value.next = next_next
            res = res.next
            counter += 1


# st = Stack()
# st.push_back(StackObj(1))
# st.push_back(StackObj(2))
# st.push_back(StackObj(3))
# print(st[0], st[1], st[2])
#
# st[0] = StackObj("obj1")
# st[1] = StackObj("obj2")
# st[2] = StackObj("obj3")
#
# print(st[0], st[1], st[2])
# print(len(st))

# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st[1] = StackObj("new obj2")
# print(st[2].data) # obj3
# print(st[1].data) # new obj2
#res = st[3] # исключение IndexError

st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
assert st[0].data == "obj11" and st[
    1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next

assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"
