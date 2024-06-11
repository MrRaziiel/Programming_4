'''
Crie uma classe abstrata, chamada MinhaAbtrata, e uma subclasse, chamada Esfera,
com o objetivo de realizar os cálculos abaixo discriminados (em referência à esfera):
Nota:
Os métodos abstratos e não abstratos devem pertencer todos à classe MinhaAbstrata.

• Área (método abstrato: calcArea())
Fórmula: 4 * PI * R2
• Diâmetro (método não abstrato: CalcDiam())

Fórmula: 2 * Raio

• Volume (método não abstrato calcVolume())
Fórmula: 4/3 π r³  <<<<----- Prof errou no volume, antes (PI * R2 * Altura)

Crie os objetos que entender necessários para testar rigorosamente o programa.
Seja livre no seu desenho e implementação.
'''

import math
from abc import ABC, abstractmethod


class MinhaAbtrata(ABC):

    def __init__(self, r):
        self.r = r

    @abstractmethod
    def calc_area(self):
        pass
        # return 4 * math.pi * (r ** 2)

    def calc_diam(self):
        return 2 * self.r

    def calc_volume(self):
        return (4 / 3) * math.pi * (self.r ** 3)
        pass
        # return math.pi * (r ** 2) * high


class Esfera(MinhaAbtrata):
    def __init__(self, r):
        MinhaAbtrata.__init__(self, r)

    def calc_area(self):
        return 4 * math.pi * (self.r ** 2)


esfera = Esfera(2)
print(f"a area da esfera é {esfera.calc_area()}")
print(f"a diametro da esfera é {esfera.calc_diam()}")
print(f"a volume da esfera é {esfera.calc_volume()}")
