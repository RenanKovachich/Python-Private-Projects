#Programa para encontrar os números divisiveis de determinado número

def print_factors(x):
    print("Os diviseveis de",x,"sao: ")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
            
num = int(input("Coloque o número que você deseja conhecer respectivo divisiveis: "))
print_factors(num)