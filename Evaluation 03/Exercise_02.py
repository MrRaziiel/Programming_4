'''
str1 = ‘a amada lisboa e o rio tejo belo encantam toda a gente’
Aplique as primitivas da classe string (index, count, in, seletor [:], len, replace,
etc.) para apresentar os seguintes resultados:
a) Imprima os carateres a partir da 1ª posição da letra b.
b) Imprima os carateres desde o início até à 1ª posição da letra b.
c) Imprima a posição (índice) da 1ª letra ‘a’
d) Imprima a quantidade de letras ‘a’ contidas nela
e) Imprima o comprimento da string (número total de carateres)
f) Substitua todos os espaços por ‘#’
g) Teste se a string contém a palavra tejo.
'''


str1 = "a amada lisboa e o rio tejo belo encantam toda a gente"
index_Of_b = str1.index("b")
print(f"A - {str1[(index_Of_b+1):]}")
print(f"B - {str1[:(index_Of_b-1)]}")
print(f"C - {str1.index("a")}")
print(f"D - {str1.count("a")}")
print(f"E - {len(str1)}")
print(f"F - {str1.replace(" ", "#")}")
print(f"G - {"tejo" in str1}")

