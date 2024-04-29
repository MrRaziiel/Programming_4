'''
Escreva um programa para calcular o ordenado líquido de um empregado de uma
determinada firma que é pago consoante o número de horas que trabalhou.
As Taxas são as seguintes.
IRS = 20% se salário bruto >= 1000€.
15% se salário bruto >= 600€ e < 1000€.
10% se salário bruto < 600€.
Horas Extras = acima de 35H cada Hora vale 1,5H (incluindo horas trabalhadas durante
o fim de semana).
Segurança Social = 11% sobre o salário bruto.

O programa deve pedir para digitar o seguinte:
Número do empregado.
Número de horas que o empregado trabalhou.
Valor Hora que o empregado é pago.
'''


def get_Asked_Value(question):
    print(question)
    input_From_User = input()
    if not input_From_User.isdigit():
        print(f"{input_From_User} It's not a number")
        input_From_User = get_Asked_Value(question)

    return float(input_From_User)


def deduce_IRS_From_Salary(_salary):
    IRS = 0
    if _salary >= 1000:
        IRS = 0.2
    elif _salary >= 600:
        IRS = 0.15
    else:
        IRS = 0.1

    _salaryDeducted = _salary * IRS
    return salary - _salaryDeducted, _salaryDeducted


salary = get_Asked_Value("What's your gross salary?")
hours = get_Asked_Value("How Many Hours did you work?")
moneyPerHour = get_Asked_Value("How much do you earn in one hour?")

salary_Deducted_IRS, salaryDeducted = deduce_IRS_From_Salary(salary)
extraHours = hours - 35.0 if hours != 0 else 0

extraHoursPay = extraHours * (moneyPerHour * 1.5) if extraHours != 0 else 0

print(f"your gross salary is:{salary}")
print(f"you work about: {hours} hours")
print(f"You earn {moneyPerHour} per hours")
print(f"You deduct for IRS:{salaryDeducted}")

if hours > 35:
    print(f"You did {extraHours} extra hours")
    print(f"You got pay {extraHoursPay} from extra hours")
else:
    print(f"You didn't do all of your work hours! left {abs(extraHours)} hours to do")

netSalary = salary_Deducted_IRS + extraHoursPay
print(f"Your Salary with extra hours is {netSalary}")

segurancaSocial = netSalary * 0.11
print(f"You discount a total of {segurancaSocial} for Segurança Social")

netSalary = netSalary - segurancaSocial
print(f"Your net salary is {netSalary}")
