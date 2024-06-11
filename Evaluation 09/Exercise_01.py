'''
Crie uma lista de 10 elementos, contendo dados à sua escolha, não digitados, mas que
sejam de diferentes tipos, tais como inteiros, floats e strings.
A partir desta lista através e através da aplicação do comando type crie três listas, cada
uma para exclusivamente um diferente tipo de dados.
Por exemplo:
Criada a sua lista:
lista1 = ['gato', 33, 'pardal', 23.7, 'macaco', ‘lia’, 45, 18.35, ‘zebra’, ‘rato’]
As seguintes três listas devem ser criadas pelo programa:
lista_strs = ['gato', 'pardal', 'macaco', ‘lia’, ‘zebra’, ‘rato’]
lista_ints = [33, 45]
lista_floats = [23.7, 18.35]
'''

lista1 = ['gato', 33, "pardal", 23.7, "macaco", "lia", 45, 18.35, "zebra", "rato", [231]]
lista_strs = []
lista_ints = []
lista_floats = []

for element in lista1:

    typeElement = str(type(element))
    if typeElement == "<class 'float'>":
        lista_floats.append(element)

    elif typeElement == "<class 'str'>":
        lista_strs.append(element)
    elif typeElement == "<class 'int'>":
        lista_ints.append(element)
    else:
        print(f" '{element}' is not string, float nor int. It's -> {type(element)}")

    """ 
    "This method is more efficient and use less code"
    
    if isinstance(element, float):
        lista_floats.append(element)
    elif isinstance(element, str):
        lista_strs.append(element)
    elif isinstance(element, int):
        lista_ints.append(element)
    else:
        print(f" {element} is not string, float nor int. It's -> {type(element)}")
    """

print(f"list strings -> {lista_strs}")
print(f"list integers-> {lista_ints}")
print(f"list floats -> {lista_floats}")
