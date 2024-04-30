'''
Crie um programa que faça pesquisas numa determinada string base com o
objetivo de substituir determinadas substrings por outras.
Exemplo do resultado que se pretende de uma execução tipo do programa:
Digite uma frase:

a ana e o aniceto foram ao cinema anadia

Digite uma substring a ser substituída:
ana
Digite uma substring de substituição:
lisboa

Resposta:

a lisboa e o aniceto foram ao cinema lisboadia

Nota:
a. O conteúdo da string base deve ficar efetivamente alterado. Ou seja,
imprimindo a string base, após as substituições, ela deve conter as
alterações que foram efetuadas.
b. Se a substring a ser substituída não for encontrada, o programa deve
informar ao utilizador dessa situação.
'''


def get_Asked_Value(question, type_of_value):
    print(question)
    input_From_User = input()
    if input_From_User.replace(" ", "") == "":
        print(f"{type_of_value} can't be empty")
        input_From_User = get_Asked_Value(question, type_of_value)

    return input_From_User


phrase = get_Asked_Value("Write a phrase please", "Phrase")
substituted_Word = get_Asked_Value("Write a word to be substitute please", "Word to be substitute")
replace_Word = get_Asked_Value("Write a word to replace please", "Word to replace")

if substituted_Word not in phrase:
    print(f"Word {substituted_Word} not found in phrase")
else:
    print(f"{phrase.replace(substituted_Word,replace_Word)}")


