'''
Faça um programa para converter uma temperatura de grau Celsius para Fahrenheit,
usando uma função, criada por si (ou seja, o programa principal deve passar à função o
valor de graus centígrados a converter e esta deve devolvê-lo o valor correspondente
em Fahrenheit). Finalmente e, por sua vez, o programa chamante deve imprimir o valor
convertido recebido.
Fórmula: °F = °C × 1.8 + 32.
'''


def convert_Celsius_To_Fahrenheit(celsius):
    return (celsius * 1.8) + 32


input_From_User = None
flag = False
fahrenheit = None

while not flag:
    print("How much temperature is it?")
    input_From_User = input()

    print(input_From_User.isdigit())
    if not input_From_User.isdigit():
        print(f'{input_From_User} is not a digit')
        flag = False
    else:
        print("skajdsa")
        flag = True
        fahrenheit = convert_Celsius_To_Fahrenheit(float(input_From_User))

print(f"The temperature {input_From_User} degrees celsius is {fahrenheit} degrees Fahrenheit ")
