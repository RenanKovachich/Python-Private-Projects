# Forca tentativa #0
palavra_secreta1 = ["c", "a", "r", "i", "o", "t", "e", "c", "a"]
letras_descobertas = []

print("\n*** Jogo da Forca ***\n")
print("Dica: é uma comida, salgada para alguns, doce para outros")

for i in range(0, len(palavra_secreta1)) :
    letras_descobertas.append("-")

acertou = False

while acertou == False :
    letra = str(input("Digite a letra: "))

    for i in range(0, len(palavra_secreta1)) :
        if letra == palavra_secreta1[i] :
            letras_descobertas[i] = letra
        
        print(letras_descobertas[i])


    acertou = True

    for x in range(0, len(letras_descobertas)) :
        if letras_descobertas[x] == "-" :
            acertou = False

print("Parabéns, você acertou a palavra!")
