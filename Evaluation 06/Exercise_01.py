'''
Escreva em Python um programa que recebe do teclado um tuplo de inteiros e
devolve um tuplo contendo apenas os algarismos pares.
Exemplo de utilização:
Insira um tuplo de inteiros positivos: 1,6,7,99,56
Algarismos pares: (6, 56)
'''


def even_Elements(__tuple):
    even_Elements_Tuple = tuple(num for num in __tuple if num % 2 == 0)
    return even_Elements_Tuple


input_From_User = input("Insira um tuplo de inteiros positivos separados por vírgula: ")
elements = input_From_User.split(',')
_tuple = tuple()

for element in elements:
    try:
        num = int(element)
    except ValueError:
        print(f"Element '{element}' is not a integer. Removed from tuple")

    else:
        _tuple += (int(element),)


print(f"Even elements: {even_Elements(_tuple)}")
