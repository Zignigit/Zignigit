class ListMath:
    def __init__(self, lst=None):
        self.lst_math = lst[:] if lst and type(lst) == list else[]
        ListMath.clear_trash(self.lst_math)

    @classmethod
    def clear_trash(cls, lst):
        indx_lst = []
        j = -1
        for i in lst:
            j += 1
            if not isinstance(i, (int, float)) or type(i) == bool:
                indx_lst.append(j)
        for k in indx_lst[::-1]:
            lst.pop(k)
        return lst

    def __add__(self, other):
        copy = self.lst_math.copy()
        for i in range(len(copy)):
            copy[i] = copy[i] + other
        return ListMath(copy)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self = self + other
        return self

    def __sub__(self, other):
        copy = self.lst_math.copy()
        for i in range(len(copy)):
            copy[i] = copy[i] - other
        return ListMath(copy)

    def __rsub__(self, other):
        copy = self.lst_math.copy()
        for i in range(len(copy)):
            copy[i] = other - copy[i]
        return ListMath(copy)

    def __isub__(self, other):
        self = self - other
        return self

    def __mul__(self, other):
        copy = self.lst_math.copy()
        for i in range(len(copy)):
            copy[i] = copy[i] * other
        return ListMath(copy)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self = self * other
        return self

    def __truediv__(self, other):
        copy = self.lst_math.copy()
        for i in range(len(copy)):
            copy[i] = copy[i] / other
        return ListMath(copy)

    def __rtruediv__(self, other):
        copy = self.lst_math.copy()
        for i in range(len(copy)):
            copy[i] = other / copy[i]
        return ListMath(copy)

    def __itruediv__(self, other):
        self = self / other
        return self




