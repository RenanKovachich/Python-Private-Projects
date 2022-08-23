#Jogo Adivinhe o Número
import random

comp_guess = random.randint(1, 100)
number_of_attempts = 0
while True:
    try:
        user_guess = int(input("Adivinhe qual é o número: "))
        
        if comp_guess == user_guess:
            number_of_attempts = number_of_attempts + 1
            print(f'Você venceu em {number_of_attempts} tentativas.')
            break
        elif user_guess < comp_guess:
            print("Muito baixo")
            number_of_attempts = number_of_attempts + 1
        else:
            print("Muito alto")
            number_of_attempts = number_of_attempts + 1
    except:
        print("Escolha um número entre 1 a 100.")
