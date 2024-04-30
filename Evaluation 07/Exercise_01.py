'''
Considere a lista numeros = [1,5,3,6,22,45,63,30,344,22,12,25,10].
Escreva um programa em Python que implementa as seguintes instruções:
a) Inverta a lista
b) Ordene a lista por ordem crescente.
c) Imprima os últimos três elementos da lista.
'''

numeros = [1, 5, 3, 6, 22, 45, 63, 30, 344, 22, 12, 25, 10]

print(f"A - Inverted list {numeros[::-1]}")
print(f"B - Sorted list {sorted(numeros)}")
print(f"C - Last three elements of list {numeros[-3:]}")
