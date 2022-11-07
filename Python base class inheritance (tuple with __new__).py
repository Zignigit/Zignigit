class TupleLimit(tuple):
    def __new__(cls, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        instance = super().__new__(cls, lst)
        return instance


    def __str__(self):
        return str(' '.join(super().__str__()[1:-1].split(', ')))

    def __repr__(self):
        return super().__repr__()



digits = list(map(float, input().split()))  # эту строчку не менять (коллекцию digits также не менять)

try:
    print(TupleLimit(digits, 5))
except Exception as e:
    print(e)