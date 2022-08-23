#Programa para descobrir o fatorial de um número Ex: 3! = 3.2.1 = 6
from math import factorial


num = int(input("Coloque o número: "))

factorial = 1

if num < 0:
    print("Desculpa, não é possível descobrir o fatorial de número negativos")
elif num == 0:
    print("O fatorial de 0 é igual a 1")
else:
    for i in range(1, num + 1):
        factorial = factorial*i
    print("O fatorial de",num,"é",factorial)
