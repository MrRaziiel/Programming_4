'''
Continuação da Prática em Manipulação de Classes e Objetos
Herança de Classes

1. Na continuação do programa anterior (Ficha 012), crie uma subclasse Professor
com o seu próprio atributo:

areaEnsino

E obtenha agora todos os cálculos (Salários Bruto e Líquido, bem como os valores
IRS e SS) para um objeto instanciado a partir desta classe derivada, repetindo
assim o programa anterior incluindo a classe herdada.
'''

import re


class Employee:
    def __init__(self, _number, _name, _grossSalary):
        self.Number = _number
        self.Name = _name
        self.GrossSalary = self.is_valid_number(_grossSalary)
        self.canBeTaxed = False if self.GrossSalary == 0 else True
        self.IRStax = self.calcIRS() if self.canBeTaxed else 0
        self.SStax = self.calcSS() if self.canBeTaxed else 0
        self.NetSalary = self.calcSalLiquido()

    def calcIRS(self, explain=True):
        if not self.isTaxable("IRS ", explain):
            return 0
        if self.GrossSalary >= 2000:
            IRS = 0.25
        elif self.GrossSalary >= 1000:
            IRS = 0.20
        else:
            IRS = 0.175

        IRStax = round(self.GrossSalary * IRS, 2)

        if explain:
            print(f"{self.Name}'s Gross Salary is {self.GrossSalary}")
            print("To Calculate IRS tax need to:")
            print(
                f"\tMultiply Gross Salary ({self.GrossSalary}) with IRS ({IRS}) that results in IRS tax of: {IRStax}\n")
        return IRStax

    def calcSS(self, explain=True):
        if not self.isTaxable("SS ", explain):
            return 0

        ssTax = round(self.GrossSalary * 0.11, 2)
        if explain:
            print("To Calculate SS tax need to:")
            print(f"\tMultiply Gross Salary ({self.GrossSalary}) with SS tha is set to '0.11' that results in SS tax "
                  f"of: {ssTax}\n")
        return ssTax

    def calcSalLiquido(self, explain=True):
        if not self.isTaxable("", explain):
            return 0

        IRStax = self.calcIRS(False)
        SSTax = self.calcSS(False)

        netSalary = self.GrossSalary - IRStax - SSTax
        print("To Calculate net Salary need to:")
        print(f"\tSubtract GrossSalary({self.GrossSalary}) with IRS tax ({IRStax}) and SS tax ({SSTax})")
        print(f"{self.Name}'s Net Salary is: {netSalary}")
        return netSalary

    def isTaxable(self, tax, explain=True):
        if not self.canBeTaxed:
            if explain:
                print(f"{self.Name} Can't be {tax}taxed because Gross Salary is {self.GrossSalary}")
            return False
        return True

    def is_valid_number(self, number):
        pattern = r'^-?\d+(\.\d+)?$'
        if isinstance(number, int) or isinstance(number, float) :
            return float(number)
        if bool(re.match(pattern, number)):
            floated = float(number)
            rounded = round(floated, 2)
            return float(number)
        else:
            return 0


# Must have the same signature of Employee!
class Professor(Employee):
    def __init__(self, _number, _name,_grossSalary):
        super().__init__(_number, _name, _grossSalary)


Ruben = Employee(10, "Ruben Amaro", 102.2)
print("____________________________________________\n")
Jose = Professor(30, "José Câmara", "10000.32")
print("____________________________________________\n")

print("Testes:")

print(f"Ruben - Calculate SS tax: {Ruben.calcSS(True)}")
print(f"Ruben - Calculate IRS tax: {Ruben.calcIRS(False)}")
print(f"Senhor José - Calculate SS tax: {Jose.calcIRS(False)}")
print(f"Senhor José - Calculate SS tax: {Jose.calcIRS(True)}")
