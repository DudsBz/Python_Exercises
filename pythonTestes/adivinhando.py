from random import randint
from time import sleep
pense = randint(0, 5)
print('Estou pensando em um número entre 0 e 5...TENTE ADIVINHAR!')
tent = int(input('Qual número você acha que estou pensando?: '))
print("PROCESSANDO RESPOSTA...")
sleep(1.5)

if tent == pense:
    print("Na mosca!!")
else:
    print("It's wrong, eu pensei no {} e não no {}".format(pense, tent))