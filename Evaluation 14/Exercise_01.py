'''
Continuação da Prática em Manipulação de Classes e Objetos

1. Crie uma calculadora com as funcionalidades básicas, tais como: somar, subtrair,
multiplicar e dividir; e algumas científicas elementares tais como: sqrt(), log(),
sin(), etc..

Nota: utilizar exceções:

1) Na leitura dos dados (se os dados são ou não numéricos)

2) Na função dividir (divisão por zero, ilegal)
'''

import math

operatorsValid = ['+', '-', '*', '/', '**']

print("\nWelcome to the calculator\n")


def calculator(results=None):
    if not results:
        while True:
            number_1 = validateNumber(input('Please enter the First number: '))
            if number_1:
                break
    else:
        number_1 = results

    number_1 = singularsOperators(number_1)

    while True:
        operator = (input(f''' \nNumber is {number_1} \nYou want apply any of : \n\t"+" for Addiction \n\t"-" for Substation \n\t"*" for Multiplication \n\t"/" for Division \n\t"**" for Potential \n\t"RESTART" to restart \n\t"EXIT" for exit\n\n INSERT:''')).lower()

        print(operator)
        inputExitOrRestart(operator)

        if operator in operatorsValid:
            break

    while True:
        number_2 = validateNumber(inputExitOrRestart(input('Please enter the Second number: ')))
        if operator == "/" and number_2 == 0:
            print("Can't divide by 0")
            pass
        if number_2:
            break

    number_2 = singularsOperators(number_2)

    calculate(number_1, number_2, operator)


def calculate(number_1, number_2, operator):
    result = None
    match operator:
        case '+':
            result = number_1 + number_2
            print(f"{number_1} + {number_2} is {result}")
        case '*':
            result = number_1 * number_2
            print(f"{number_1} * {number_2} is {result}")
        case '/':
            result = number_1 / number_2
            print(f"{number_1} / {number_2} is {result}")
        case '**':
            result = number_1 ** number_2
            print(f"{number_1} ** {number_2} is {result}")
    again(result)


def validateNumber(number):
    inputExitOrRestart(number)
    try:
        number = float(number)
    except:
        return False
    return number


def singularsOperators(number):
    operator = inputExitOrRestart(input(f'''Number is {number} \nYou want apply any of : \n\t"SQRT" for √ \n\t"LOG" for log() \n\t"SIN" for sine \n\t"COS" for cosine \n\t"TAN" for Tangent \n\t"RESTART" to Restart \n\t"NO" for not apply any \n\t"exit" for exit \n\nInsert: ''')).lower()

    match operator:
        case "sqrt":
            result = math.sqrt(number)
            print(f"√ of {number} is {result}")
            singularsOperators(result)
        case "log":
            result = math.log(number, base=10)
            print(f"log of {number} is {result}")
            singularsOperators(result)

        case "sin":
            result = math.sin(math.radians(number))
            print(f"sin of {number} is {result}")
            singularsOperators(result)

        case "cos":
            result = math.cos(math.radians(number))
            print(f"cos of {number} is {result}")
            singularsOperators(result)
        case "tan":
            result = math.cos(math.radians(number))
            print(f"cos of {number} is {result}")
            singularsOperators(result)
        case _:
            result = number

    return result


def again(number):
    while True:
        input_From_User = inputExitOrRestart(input('''
                1 for operate another number?
                2 for Restart
                3 for Exit '''))
        if validateNumber(input_From_User):
            input_From_User = float(input_From_User)

            match input_From_User:
                case 1:
                    calculator(number)
                case 2:
                    calculator()
                case 3:
                    exit()
                case _:
                    again(number)
            break


def inputExitOrRestart(input_From_User):
    if input_From_User.lower() == "exit":
        exit()
    elif input_From_User.lower() == "restart":
        calculator()
    else:
        return input_From_User


calculator()
