
from card import Card
from layer import Layer


class Tabela:
    def __init__(self, name):
        self.name = name
        self.layers = []
        self.completion = 0

    def add_layer_behind(self):
        layer = Layer()
        self.layers.insert(0, layer)

    def add_layer_ahead(self):
        layer = Layer()
        self.layers.append(layer)

    def no_layers(self):
        if self.layers == []:
            self.add_layer_ahead()
