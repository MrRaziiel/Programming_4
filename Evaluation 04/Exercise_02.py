'''
 Crie uma lista, chamada lista1, com os seguintes valores: ‘Iva’, 25, ‘Rui’, 19,
‘Rato’, ‘abc’, 33
a) Imprima toda a lista
b) Imprima os elementos de 2 a 4 (inclusive)
c) Imprima os elementos do início até ao elemento 3 (exclusive)
d) Imprima os elementos de 3 até ao fim da lista
e) Crie uma nova lista, com valores à sua escolha, chamada lista2, e junte-a à
lista1, criando assim uma nova lista. Imprima a nova lista.
'''

lista1 = ["Iva", 25, "Rui", 19, "Rato", "abc", 33]


print(f"A- {lista1}")
print(f"B- {lista1[1:5]}")
print(f"C- {lista1[:2]}")
print(f"D- {lista1[2:]}")
lista2 = ["Vou", "Ter", ["Boa", {"Nota": 20}]]
lista1.extend(lista2)
print(f"E- {lista1}")
