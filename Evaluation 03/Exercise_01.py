'''
Escreva um programa que leia uma string digitada e que seguidamente mostre
no ecrã as ocorrências de cada vogal. Por exemplo, digitando a frase Campus
Lumiar, a resposta deve ser:
Ocorrências da Vogal a: 2
Ocorrências da Vogal e: 0
Ocorrências da Vogal i: 1
Ocorrências da Vogal o: 0
Ocorrências da Vogal u: 2
'''

counter_vogals = 0
counter_vogals_Acentuadas = 0

vogais = ['a', 'e', 'i', 'o', 'u']
vogais_acentuadas = ['á', 'é', 'í', 'ó', 'ú', 'â', 'ê', 'ô', 'à', 'ã']

word = None

while not word:
    word = str(input("Enter a word: "))
    if word.isspace() or word == "":
        print("Invalid format word, please word can't be empty")
        word = None

for index, character in enumerate(word, 1):
    if character.lower() in vogais:
        counter_vogals += 1
        print(f'Ocorrências da Vogal {character} in index: {index}')
    if character.lower() in vogais_acentuadas:
        counter_vogals_Acentuadas += 1
        print(f'Ocorrências da Vogal acentuada {character} no index: {index}')

    if character.isdigit():
        print(f'Encontrado um inteiro "{character}" no index {index}')

if counter_vogals == 0:
    print(f'Não Ocorrências Vogais e nem Vogais acentuadas ')
    print(f'Não Ocorrências Vogais acentuadas ')
else:
    print(f'Total de vogais encontradas foi: {counter_vogals}')
if counter_vogals_Acentuadas > 0:
    print(f'Total de vogais acentuadas encontradas foi: {counter_vogals_Acentuadas}')
