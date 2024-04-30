'''
Considere o tuplo numeros = (10,15,3,6,99,45,63,30,344,22,4,25,10).
Escreva um programa em Python que implementa as seguintes instruções:

a) Apresenta o comprimento do tuplo.
b) Apresenta o máximo e mínimo do tuplo.
c) Cria um novo tuplo numeros3 juntando numeros com numeros2:
numeros2 = (21, 53, 23, 54,22,2,1,13)
d) Imprime os elementos de índice ímpar.
e) Imprime os elementos que são múltiplos de 5.
'''

numeros = (10, 15, 3, 6, 99, 45, 63, 30, 344, 22, 4, 25, 10)

print(f"A - lenght of tuple: {len(numeros)}")
print(f"B - minimum value of tuple: {min(numeros)} and maximum value of tuple: {max(numeros)} ")
numeros2 = (21, 53, 23, 54, 22, 2, 1, 13)
numeros3 = numeros + numeros2
print(f"C - Tuple numeros3: {numeros3}")

odd_Elements_Tuple = tuple(num for num in numeros3 if num % 2 != 0)

tuple_len = len(odd_Elements_Tuple)
if tuple_len == 1:
    print(f"D - The odd number is: {odd_Elements_Tuple}" )

elif tuple_len == 0:
    print(f"D - No odd numbers found")
else:
    print(f"D - The odd numbers are: {odd_Elements_Tuple}" )

elements_divided_By_5_Tuple = tuple(num for num in numeros3 if num % 5 == 0)

print(f"E - Elements multiply by 5 are: {elements_divided_By_5_Tuple}" )

