'''
Crie um dicionário para guardar informação sobre animais de estimação.
Cada chave é o nome de um animal e cada valor é a espécie de animal.
Por exemplo: ‘Ziggy’: ’canário’.

1. Comece por definir um dicionário base com os seguintes cinco pares chave-
valor:

Ziggy: canario, Pluto: cao, Kitty: gato, Nemo: peixe, Mickey: rato
2. Seguidamente, peça ao utilizador para adicionar dados de novos animais.
Deverá parar a inserção quando o utilizador inserir a palavra 'fim’.
3. Desenvolva um mecanismo de pesquisa que imprima um determinado par
Chave-Valor a pedido do utilizador, a partir de uma dada chave.
'''

animals = {"Ziggy": "canario", "Pluto": "cao", "Kitty": "gato", "Nemo": "peixe", "Mickey": "rato"}


def get_Asked_Value(question, type_of_value):
    print(question)
    input_From_User = input()
    if input_From_User.replace(" ", "") == "":
        print(f"{type_of_value} can't be empty")
        input_From_User = get_Asked_Value(question, type_of_value)

    return input_From_User


flag = False

while not flag:
    print("Form to add a new animal")
    print("To stop adding just write 'fim' whenever \n")
    name_Of_Animal = get_Asked_Value("First what's the name of the animal?", "Name")
    if name_Of_Animal.lower() != "fim":
        type_Of_Animal = get_Asked_Value("Second what's the type of the animal?", "Type")
    else:
        break
    if type_Of_Animal.lower() != "fim":
        animals[name_Of_Animal] = type_Of_Animal
        print(f"Add a new animal! {name_Of_Animal}:{type_Of_Animal}\n")
    else:
        break

print(f"The new dictionary is {animals} \n")

while True:
    print("Need to find an animal? write a name of the animal")
    print("To stop adding just write 'fim' whenever")
    query = input()
    if query.lower() == 'fim':
        break

    if query in animals.keys():
        print(f"The animal {query} is a {animals[query]}\n")
    else:
        print(f"The animal {query} is not in dictionary, retry.\n")

while True:
    print("Need to find an animal? write the specie of animal")
    print("To stop adding just write 'fim' whenever")
    query = input()
    if query.lower() == 'fim':
        break

    name_Got_From_Query = ""
    for key, value in animals.items():
        if value == query:
            name_Got_From_Query = key

    if name_Got_From_Query:
        print(f"The name of {query} is {name_Got_From_Query}\n")
    else:
        print(f"The type of animal {query} is not in dictionary, retry.\n")

print("GoodBye")
