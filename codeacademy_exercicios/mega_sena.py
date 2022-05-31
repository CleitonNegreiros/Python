# Geração das dezenas da mega-sena
import random

all = list(range(1,61))

dezenas = random.sample(all, 6)
dezenas.sort()
print("Seu jogo será: " + str(dezenas) + '\nBoa Sorte!')