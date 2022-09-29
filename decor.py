class InputValues:
    def __init__(self, render):
        self.__render = render

    def __call__(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            return list(map(self.__render, func(*args, **kwargs).split()))

        return wrapper


class RenderDigit:
    def __call__(self, string, *args, **kwargs):
        try:
            return int(string)
        except:
            return None



@InputValues(RenderDigit())
def input_dg():
    return input()


print(input_dg())
