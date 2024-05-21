'''
Escreva um programa que faça a leitura de um ficheiro de texto e que,
seguidamente, volte a gravar o mesmo ficheiro, mas somente contendo as
palavras únicas (sem as palavras repetidas).
Inclua exceções e tratamento de quaisquer anomalias que possam ocorrer com
a abertura do ficheiro.
'''
import os
import string

def remove_Punctuation(word):
    return word.translate(str.maketrans('', '', string.punctuation))
def get_Unique_Words(string_Entered):
    newText = []
    uniquesWords = {}
    for line in text_Inside_File:
        newLine = []
        for word in line.split(" "):
            word_Without_Punctuation = remove_Punctuation(word)
            if word_Without_Punctuation not in uniquesWords:
                uniquesWords[word_Without_Punctuation] = 0
            if uniquesWords[word_Without_Punctuation] == 0:
                newLine.append(word)
                uniquesWords[word_Without_Punctuation] = 1
        newText.append(newLine)
    return newText

def format_Array_To_String(newText):
    text_To_Show = ""
    for line in newText:
        helper = ' '.join(line).lstrip(' ')
        text_To_Show += f"{helper} \n"
    print(text_To_Show)
    return text_To_Show


file_Path = "FreeText2.txt"

if os.path.isfile(file_Path):
    # file exists
    try:
        file = open(file_Path, "r", encoding='utf-8')
    except Exception as e:
        exit(e)

    try:
        text_Inside_File = str(file.read()).split('\n')

    except Exception as e:
        file.close()
        exit(f"Can't open the file \n {e}")
    finally:
        file.close()

else:
    exit("file doesn't exist")


word_In_Array = get_Unique_Words(text_Inside_File)
word_To_Show = format_Array_To_String(word_In_Array)

try:
    file = open(file_Path, 'w', encoding='utf-8')
    file.write(word_To_Show)

    print("unique words write in the same file successfully")

except Exception as e:
    exit(e)
finally:
    file.close()

