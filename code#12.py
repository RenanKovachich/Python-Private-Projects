#Programa para sortear uma carta de baralho aleatória
import random
cards = ["Ouros", "Copas", "Espadas", "Paus"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10,
         "Valete", "Dama", "Rei", "Ás"]

def pick_a_card():
    card = random.choices(cards)
    rank = random.choices(ranks)
    return(f"{rank} de {card}")

print(pick_a_card())