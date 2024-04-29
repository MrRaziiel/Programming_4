'''
Escreva um programa que, usando ciclos, peça ao utilizador para digitar um número
inteiro pequeno, correspondente a um número de linhas, para desenhar um padrão de
asteriscos, do tipo abaixo ilustrado em dois exemplos:
'''


def get_Asked_Value(question):
    print(question)
    input_From_User = input()
    if not input_From_User.isdigit():
        print(f"{input_From_User} It's not a number")
        input_From_User = get_Asked_Value(question)
    if int(input_From_User) >= 10:
        print(f"it's not below 10")
        input_From_User = get_Asked_Value(question)

    return int(input_From_User)


number = get_Asked_Value("Please write a number below 10: ")

for i in range(1, (number + 1)):
    print("*" * i)
