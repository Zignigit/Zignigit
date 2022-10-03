class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head is None:
            self.head = obj
        if self.tail is not None:
            self.tail.next = obj
            prevq = self.tail
            self.tail = obj
            self.tail.prev = prevq
        else:
            self.tail = obj

    def remove_obj(self, indx):
        if self.__len__() == 1 and indx == 0:
            self.head = None
            self.tail = None
        if self.__len__() > 0 and indx == 0:
            self.head = self.head.next
            self.head.prev = None
        if self.__len__() > 2 and indx != 0:
            n = 0
            remobj = self.head
            while n != indx:
                remobj = remobj.next
                n += 1
            self.tail = remobj.prev
            self.tail.next = None
        if self.__len__() == 2 and indx == 1:
            self.head.next = None
            self.tail = self.head


    def __len__(self):
        count = 0
        cur_obj = self.head
        while self.head and cur_obj.next:
            cur_obj = cur_obj.next
            count += 1
        if self.head:
            return count+1
        else:
            return 0

    def __call__(self, indx, *args, **kwargs):
        c = 0
        obj = self.head
        while c != indx:
            obj = obj.next
            c += 1
        return obj.data


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None


    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__next = obj

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if type(obj) in (ObjList, type(None)):
            self.__prev = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, obj):
        if isinstance(obj, str):
            self.__data = obj





ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"