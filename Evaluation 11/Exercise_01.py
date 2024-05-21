'''
Prática em Manipulação de Ficheiros

1 Desenvolva um programa que aplique as técnicas de programação inerentes aos
Ficheiros de Texto para a obtenção de um determinado conjunto de cálculos
estatísticos a partir de um ficheiro de texto livre, criado por si, sob a forma de
ocorrências/quantidades, conforme abaixo descrito:

a) De cada vogal (frequência discriminada das ocorrências de cada vogal).
b) Das consoantes (totalidade das consoantes)
c) Das palavras (totalidade das palavras)
d) Das linhas

Inclua exceções e tratamento de quaisquer anomalias que possam ocorrer com
a abertura do ficheiro.
'''

import os

vowels = 'aeiouáéíóúãẽĩõũàèìòùâêîôûäëïöüÁÉÍÓÚÃẼĨÕŨÀÈÌÒÙÂÊÎÔÛÄËÏÖÜ'


def count_vowels(text):
    vowel_counts = {vowel: text.count(vowel) for vowel in vowels if vowel in text}
    return vowel_counts


def count_consonants(text):
    consonant_count = sum(text.count(consonant) for consonant in text if consonant not in vowels)
    return consonant_count


file_Path = "FreeText.txt"

if os.path.isfile(file_Path):
    # file exists
    try:
        file = open(file_Path, "r", encoding='utf-8')
    except Exception as e:
        exit(e)

    try:
        text_Inside_File = str(file.read())

    except Exception as e:
        file.close()
        exit(f"Can't open the file \n {e}")
    finally:
        file.close()

else:
    exit("file doesn't exist")

text_Without_Spaces = text_Inside_File.replace(" ", "")
number_Of_Consonant = count_consonants(text_Without_Spaces)
list_Vowels = count_vowels(text_Without_Spaces)

print("A - Vogais")
for vowel, count in list_Vowels.items():
    print(f"{vowel}: {count}")
print("______")
print(f"B - Total of consonant in text is: {number_Of_Consonant}")
print(f"C - Total of words in text is: {len(text_Inside_File.split())}")
print(f"D - Total of line in text is: {len(text_Inside_File.split("\n"))}")
