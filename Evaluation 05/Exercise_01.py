'''
Escreva um programa que leia um conjunto de cinco valores do tipo float
digitados, carregando-os, um a um, num vetor unidimensional de cinco
elementos e, que, seguidamente, passe-o (o vetor) a uma função.

Esta, por sua vez, deve calcular e devolver ao programa chamante a quantidade
(número de ocorrências) de valores acima de 20.00.

Por sua vez, o programa chamante deve imprimir este resultado (o valor que
foi devolvido).
'''


def how_Many_Values_More_Than_20(_vector):
    values_more_Than_20 = [lambda: x for x in _vector if x > 20.00]
    return len(values_more_Than_20)


def get_Asked_Value(question):
    print(question)
    input_From_User = input()
    if not input_From_User.isdigit():
        print(f"{input_From_User} It's not a number")
        input_From_User = get_Asked_Value(question)

    return float(input_From_User)


print("Please write 5 numbers: ")

vector = []
for i in range(1, 6):
    vector.append(get_Asked_Value(f"Write the {i}ª number"))

print(f"The amount of values that the value is more than 20.00 is: {how_Many_Values_More_Than_20(vector)}")
