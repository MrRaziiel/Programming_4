'''
Pretende-se que desenhe e implemente uma pequena aplicação em Python, chamada
Meu Compressor Básico (MCB).

O MCB deve funcionar da seguinte forma:
1. Uma lista de palavras únicas deve ser criada a partir de uma string digitada.

Por exemplo, dada a string:
“A iva e a zita e a ana dizem ola ana ola iva ola”
 _______________________________________________________
 |   a iva e a zita e a ana dizem ola ana ola iva ola  |
 |  0  1  2 3  4   5 6  7    8    9  10  11   12  13   |
 |_____________________________________________________|
A seguinte lista de palavras únicas deve ser criada:

                        a
                        iva
                        e
                        zita
                        ana
                        dizem
                        ola

Recorde-se que uma lista é rica em métodos (append, insert, remove, index,
count, clear, etc.) que facilitam o trabalho da programação com esta estrutura.
2. A string base deve ser completamente destruída.
3. Finalmente, a partir da lista de palavras únicas deve reconstruir a string original
(que foi completamente destruída, não podendo haver uma cópia dela em parte
nenhuma).

4. Naturalmente, no seu algoritmo que vai desenvolver, o programa deve guardar
as posições de cada palavra repetida de forma a poder reinseri-las nos locais
apropriados.
'''

rebuild_string = ""


def list_of_unics_and_positions(string_Entered):
    words = string_Entered.split()
    list_unic = []
    positions = []

    for word in words:
        if word not in list_unic:
            list_unic.append(word)
        positions.append(list_unic.index(word))

    return list_unic, positions


def reconstruct_String(list_unic, positions):
    word_Reconstructed = [list_unic[i] for i in positions]
    return ' '.join(word_Reconstructed)


def MCB(string_Entered):
    # First of create two list, one unics word and second one for the positions
    list_Unic, positions = list_of_unics_and_positions(string_Entered)

    # Second: Destroy the string original
    string_Entered = ""

    # Third: Rebuild the string original
    return reconstruct_String(list_Unic, positions)


string_Base = "A iva e a zita e a ana dizem ola ana ola iva ola"

rebuild_String_To_Show = MCB(string_Base)
string_Base = ""

print(rebuild_String_To_Show)
