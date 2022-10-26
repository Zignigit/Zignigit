class Layer:
    def __init__(self, next_layer=None, name='Layer'):
        self.next_layer = next_layer
        self.name = name

    def __call__(self, *args, **kwargs):
        self.next_layer = args[0]
        return args[0]


class Input(Layer):
    def __init__(self, inputs, name='input'):
        super().__init__()
        self.inputs = inputs
        self.name = name


class Dense(Layer):
    def __init__(self, inputs, outputs, activation, name='Dense'):
        super().__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation
        self.name = name


class NetworkIterator:
    def __init__(self, network):
        self.network = network
        self.iter = self.network
        self.counter = 0

    def __iter__(self):
        self.iter = self.network
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            temp = self.network
            self.counter += 1
            return temp
        if self.iter.next_layer:
            self.iter = self.iter.next_layer
            return self.iter
        raise StopIteration




# first_layer = Layer()
# next_layer = first_layer(Layer())
# next_layer = next_layer(Layer())
network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))
for x in NetworkIterator(network):
    print(x.name)