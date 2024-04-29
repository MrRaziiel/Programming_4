'''
Considere a lista numeros = [1,5,3,6,22,45,63,30,344,22,12,25,10].
Escreva um programa em Python que implementa as seguintes instruções:
a) Apresenta o comprimento da lista.
b) Apresenta o máximo e mínimo da lista.
c) Acrescenta ao final da lista os elementos da lista:
numeros2 = [21,53,23,54,22,2,1,13]
d) Altera a lista numeros por forma a que fique ordenada.
e) Indica qual o elemento que aparece mais, indicando o índice da primeira
ocorrência na lista.
f) Imprime os elementos da lista numa só linha e separados por “-”.
g) Imprime os elementos de índice ímpar.
h) Imprime os elementos que são múltiplos de 5.
'''

from collections import Counter


def number_More_Frequently_Appear(array):
    counter = Counter(array)
    return counter.most_common(1)[0][0]


list_Of_Numbers = [1, 5, 3, 6, 22, 45, 63, 30, 344, 22, 12, 25, 10]

print(f"A - Lenght of array is {len(list_Of_Numbers)}")
print(f"B - Minimum number is {min(list_Of_Numbers)} and maximum is {max(list_Of_Numbers)}")

list_Of_Numbers.extend([21, 53, 23, 54, 22, 2, 1, 13])
print(f"C - After add second list, the first one is now:{list_Of_Numbers}")

print(f"D - List sorted {sorted(list_Of_Numbers)}")

print(f"E - Number that appear more frequently {number_More_Frequently_Appear(list_Of_Numbers)}")

string_Numbers = ""
numbers_In_Odd_Index = []
numbers_Could_Be_Divided_By_5 = []
for index, number in enumerate(list_Of_Numbers, 1):
    string_Numbers += str(number) + "-" if index < len(list_Of_Numbers) else str(number)
    if index % 2 == 1:
        numbers_In_Odd_Index.append(number)
    if number % 5 == 0:
        numbers_Could_Be_Divided_By_5.append(number)

print(f"F - Number with '-' in same line: {string_Numbers}")
print(f"G - Numbers in Odd Indexes: {numbers_In_Odd_Index}")
print(f"G - Numbers can be divided by 5: {numbers_Could_Be_Divided_By_5}")
