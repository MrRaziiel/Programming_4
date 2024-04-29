'''
 Crie um programa, que use uma função, criada por si, para testar se um determinado
número passado como parâmetro é ou não primo. A função deve devolver o valor 1 ao
programa chamante no caso de o número ser primo ou o valor 0 no caso de não o ser.
Por sua vez, o programa chamante deve informar no ecrã se o número em análise é
ou não primo.
Nota:
Números Primos:
São os números naturais que têm apenas dois divisores diferentes, o 1 e ele mesmo, ou
seja, o 1 e o próprio.
Exemplo:
O Valor 2 é primo porque tem apenas os divisores 1 e 2.
O Valor 1 não é primo porque ele tem apenas um divisor que é ele mesmo.
O Valor 2 é o único par que é primo.

'''

import math


def is_prime(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    elif n % 2 == 0:
        return 0
    else:
        sqrt_n = int(math.sqrt(n))
        for index in range(3, sqrt_n + 1, 2):
            if n % index == 0:
                return 0
        return 1


# Test the function
number = 1

print(f"{number} is prime.") if is_prime(number) else print(f"{number} is not prime.")
