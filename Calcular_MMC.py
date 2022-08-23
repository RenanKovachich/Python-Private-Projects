#Prog para calcular MMC
from pickle import TRUE


def mmc(a,b):
    
    if a > b:
        greater = a
    elif b > a:
        greater = b
    while(True):
        if ((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater = greater + 1
    return lcm
a = int(input("Qual o valor do 1º número: "))
b = int(input("Qual o valor do 2º número: "))
print(mmc)
