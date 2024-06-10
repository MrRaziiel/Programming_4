'''
Baseando-se nas Fichas 012 e 013, adapte os dois programas na criação de um novo
programa que acomode o seguinte:
• O atributo numero deve ser private.
• O atributo nome deve ser protected.
• Crie dois objetos emp1 e prof1.
O objeto emp1 deve ser instaciado a partir da classe base Empregado.
O objeto prof1 deve ser instaciado a partir da classe derivada Professor.

Obtenha agora todos os cálculos (Salários Bruto e Líquido, bem como os valores
IRS e SS) para os dois objetos, produzindo no ecrã a seguinte resposta tipo:

Dados Objeto emp1:
Numero: 12345
Nome: Ana Rita
Salário Bruto: $$$$$$.$$
Desconto IRS: $$$$.$$
Desconto Segurança Social: $$$$.$$
Salário Líquido: $$$$$$.$$

Dados Objeto prof1:
Numero: 33366
Nome: Rui Alves
Área de Ensino: Matemática
Salário Bruto: $$$$$$.$$
Desconto IRS: $$$$.$$
Desconto Segurança Social: $$$$.$$
Salário Líquido: $$$$$$.$$
'''

import re


class Employee:
    def __init__(self, _number, _name, _grossSalary):
        self.__Number = _number
        self._Name = _name
        self.GrossSalary = self.is_valid_number(_grossSalary)
        self.canBeTaxed = False if self.GrossSalary == 0 else True
        self.IRStax = self.calcIRS() if self.canBeTaxed else 0
        self.SStax = self.calcSS() if self.canBeTaxed else 0
        self.NetSalary = self.calcSalLiquido()

    def getNumber(self):
        return self.__Number
    def calcIRS(self):
        if not self.isTaxable("IRS "):
            return 0
        if self.GrossSalary >= 2000:
            IRS = 0.25
        elif self.GrossSalary >= 1000:
            IRS = 0.20
        else:
            IRS = 0.175

        IRStax = round(self.GrossSalary * IRS, 2)

        return IRStax

    def calcSS(self):
        if not self.isTaxable("SS "):
            return 0

        ssTax = round(self.GrossSalary * 0.11, 2)
        return ssTax

    def calcSalLiquido(self):
        if not self.isTaxable(""):
            return 0

        IRStax = self.calcIRS()
        SSTax = self.calcSS()

        netSalary = self.GrossSalary - IRStax - SSTax
        return netSalary

    def isTaxable(self, tax):
        if not self.canBeTaxed:
            return False
        return True

    def is_valid_number(self, number):
        pattern = r'^-?\d+(\.\d+)?$'
        if isinstance(number, int) or isinstance(number, float):
            return float(number)
        if bool(re.match(pattern, number)):
            floated = float(number)
            rounded = round(floated, 2)
            return float(number)
        else:
            return 0


class Professor(Employee):
    def __init__(self, _number, _name, _grossSalary, _teachingArea):
        super().__init__(_number, _name, _grossSalary)
        self.TeachingArea = _teachingArea


emp1 = Employee(12345, "Ana Rita", "2000")
prof1 = Professor(33366, "Rui Alves", "10000.32", "Matemática")

persons = [emp1, prof1]

for person in persons:
    print(f"Number: {person.getNumber()}")
    print(f"Name: {person._Name}")
    if hasattr(person,"TeachingArea"):
        print(f"Teaching Area: {person.TeachingArea}")
    print(f"Gross Salary:{person.GrossSalary}")
    print(f"IRS CUT:{person.IRStax}")
    print(f"Segurança Social CUT:{person.SStax}")
    print(f"Net Salary CUT:{person.NetSalary}")
    print("__________________________")
