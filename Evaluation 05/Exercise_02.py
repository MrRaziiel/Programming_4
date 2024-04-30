'''
Escreva um programa que crie uma matriz 3X4 (3 linhas/4 colunas) de valores
inteiros e passe-a a uma função para que devolva a quantidade de valores
negativos nela contidos. Por sua vez, o programa chamante deve imprimir no
ecrã o valor devolvido.
'''


def how_Many_Values_Are_Negative(_vector):
    countNegatives = 0
    for i in range(len(_vector)):
        for j in range(len(_vector[i])):
            countNegatives += 1 if _vector[i][j] < 0 else 0
    return countNegatives


vector = [-1, -2, -3, -4], [-1, -421, -312, -124], [-421, -421, -231312, -321312]

print(f"The following array bidimentional: '{vector}' Have {how_Many_Values_Are_Negative(vector)} negative values")
