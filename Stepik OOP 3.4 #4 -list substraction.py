class NewList:
    def __init__(self, lst=None):
        self.lst = lst[:] if lst and type(lst) == list else []

    def __sub__(self, other):
        if isinstance(self, NewList):
            copy = self.lst.copy()
        else:
            copy = self.copy()
        if isinstance(other, NewList):
            other = other.lst
        l1 = []
        l2 = []
        indx = -1
        for i in self.lst:
            indx += 1
            jindx = -1
            for j in other:
                jindx += 1
                if type(i) == type(j) and i == j and jindx not in l2 and indx not in l1:
                    l1.append(indx)
                    l2.append(jindx)
        for i in l1[::-1]:
            copy.pop(i)

        return NewList(copy)

    def __isub__(self, other):
        self = self - other
        return self

    def __rsub__(self, other):
        return NewList(other) - self

    def get_list(self):
        if isinstance(self, NewList):
            return self.lst
        if isinstance(self, list):
            return self
