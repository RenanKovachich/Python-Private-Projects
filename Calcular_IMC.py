#Calcular IMC
altura = float(input("Diga sua altura em centimetros: "))
peso = float(input("Dia seu peso em kilograma: "))

altura = altura/100

IMC = peso/(altura*altura)
print("Seu IMC é de: ",IMC)

if(IMC > 0):
    if(IMC<=16):
        print("Você está muito abaixo do peso")
    elif(IMC<=18.5):
        print("Você está abaixo do peso")
    elif(IMC<=25):
        print("Você está saudável")
    elif(IMC<=30):
        print("Você está acima do peso")
    else:
        print("Você está muito acima do peso")
else: 
    print("Insira valores corretamente")
