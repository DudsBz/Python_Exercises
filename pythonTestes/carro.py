from random import randint

limit = randint(60, 160)
print("Seu carro passou por um radar e se você passou de 80 KM a multa vai ser de 7 reais por KM. A velocidade atingida foi de {}".format(limit))
if limit > 80:
    multa = (limit - 80) * 7
    print("Você passou do limite de velocidade, a multa é de R${},00".format(multa))
else:
    print("Pratique sempre pilotagem defensiva, parabéns")
