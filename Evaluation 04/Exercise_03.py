'''
Escreva um programa que calcule o volume de uma esfera, usando uma função
criada por si. A função deve calcular o volume da esfera e devolver o resultado
ao programa chamante que, por sua vez, deve imprimi-lo.
A fórmula matemática é a seguinte:
    Volume     = (4*Pi * R^3) /3
        esfera
Exemplo de como aplicar a fórmula:
Vejamos o caso de uma esfera que possua um raio com a medida de 5 cm. Então,
o volume dessa esfera deve ser calculado da seguinte fórmula.
    v = (4*3.14*5^3) / 3
    v = (4*3.14*125) / 3
    v = 1570 / 3
    v ~= 523,33cm^3
A esfera possui 523,33 cm³ de volume
'''

import math

pi = math.pi


def calculate_Volume_Sphere(radius):
    if radius == 0:
        return 0

    return ((4 * pi) * (math.pow(radius,3))) / 3


print(f"The sphere has a volume of {round(calculate_Volume_Sphere(5), 3)}cm³")
