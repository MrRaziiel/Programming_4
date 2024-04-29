'''
Escreva um programa que leia sete valores de temperaturas digitados (use um ciclo) e
que seguidamente calcule as médias das temperaturas cujos valores estejam
compreendidos entre 18 e 28 graus, ambos inclusive, bem como de todas as
temperaturas. Portanto, é pedido os cálculos de duas médias, uma dos valores entre 18
e 28 graus e outra de todos os valores (incluindo assim os que estejam também entre
18 e 28 graus).
'''


how_Many_Temperatures = 7
average = 0
average_18_to_28 = 0
index = 1
counterAverage_18_to_28 = 0

while index <= how_Many_Temperatures:
    print(f"write the {index}º temperature")
    input_From_User = input()
    if input_From_User.isdigit():
        temperature = float(input_From_User)
        index += 1
        average += temperature

        if 18 <= temperature <= 28:
            counterAverage_18_to_28 += 1
            average_18_to_28 += temperature

    else:
        print(f"'{input_From_User}' is not a integer")

    average = average / how_Many_Temperatures if average != 0 else 0
    average_18_to_28 = average_18_to_28 / counterAverage_18_to_28 if (counterAverage_18_to_28 != 0 or average_18_to_28
                                                                      != 0) else 0
if counterAverage_18_to_28 != 0:
    print(f"Average is: {round(average, 2)}\nAverage between 18 e 28 {round(average_18_to_28, 2)}")
else:
    print(f"Average is: {round(average, 2)}\nNo Temperature was found between 18 and 28")
