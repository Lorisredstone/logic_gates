import sys
from enum import Enum, auto

class Types(Enum):
    AND = auto()
    OR = auto()
    NOT = auto()
    XOR = auto()
    XNOR = auto()
    NAND = auto()
    NOR = auto()

class Plaque:
    def __init__(self):
        self.liste_portes : list[Porte, ] = []
        self.contents : list[int, ] = {}
        self.end : bool = False
    def __repr__(self):
        return str([x.get_txt(self.contents) for x in self.liste_portes])
    def set(self, liste_portes):
        self.liste_portes = liste_portes
    def add_porte(self, porte):
        self.liste_portes.append(porte)
    def input(self, inputs):
        for id, valeur in inputs:
            self.contents[id] = valeur
    def step(self):
        nouveau_contents = {}
        for id, value in self.contents.items():
            nouveau_contents[id] = value
        for porte in self.liste_portes:
            nouveau_contents[porte.output] = porte.process(porte.type, porte.input1, porte.input2, self.contents)
        self.contents = {}
        for id, value in nouveau_contents.items():
            self.contents[id] = value
        self.end = self.contents[len(self.contents)-1]

class Porte:
    def __init__(self, type, input1, input2, output):
        self.type = type
        self.input1 = input1
        self.input2 = input2
        self.output = output
    def get_txt(self, content):
        return f"{str(self.type)[6:]}({content[self.input1]}, {content[self.input2]}) = {content[self.output]}"
    def process(self, type, input1, input2, content):
        input1 = content[input1]
        input2 = content[input2]
        match type:
            case Types.AND:
                return input1 and input2
            case Types.OR:
                return input1 or input2
            case Types.NOT:
                return not input1
            case Types.XOR:
                return input1 != input2
            case Types.XNOR:
                return input1 == input2
            case Types.NAND:
                return not (input1 and input2)
            case Types.NOR:
                return not (input1 or input2)
        
plaque = Plaque()
plaque.add_porte(Porte(Types.OR, 0, 1, 2))
plaque.add_porte(Porte(Types.AND, 1, 2, 3))
plaque.input([(0, 0), (1, 1), (2, 0), (3, 0)])
while not plaque.end:
    plaque.step()
print(plaque.contents)
