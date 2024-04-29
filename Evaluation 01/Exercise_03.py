'''
Crie um programa que leia três valores inteiros digitados para três variáveis,
nomeadamente, n1, n2 e n3 e que, seguidamente, determine qual é o seu valor
intermédio.
Nota:
Não é a média que é pedida, mas sim o valor do intermédio!
Assim, por exemplo, dados os valores: 7, 8 e 6, digitados para as variáveis n1, n2 e n3,
respetivamente, a resposta é 7 (o valor 7 está no meio de 6 e 8). Por sua vez, no caso de
serem digitados os valores 9, 3 e 5, para as variáveis n1, n2 e n3, respetivamente, a
resposta é 5. Use uma estrutura condicional (ou seja, não pode ordenar os números e
ler o valor que está no meio dos três)
'''


def get_Asked_Value(question):
    print(question)
    input_From_User = input()
    if not input_From_User.isdigit():
        print(f"{input_From_User} It's not a number")
        input_From_User = get_Asked_Value(question)

    return int(input_From_User)


number1 = get_Asked_Value("Write a first number integer:")
number2 = get_Asked_Value("Write a Second number integer:")
number3 = get_Asked_Value("Write a Third number integer:")

if number1 <= number2 <= number3 or number3 <= number2 <= number1:
    intermediate = number2
elif number2 <= number1 <= number3 or number3 <= number1 <= number2:
    intermediate = number1
else:
    intermediate = number3

print("the intermediate value is:", intermediate)
