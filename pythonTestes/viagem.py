
print("O preço da passgem varia de acordo com a distância da viagem. ")
print("")
print("R$0,50 por KM para viagens de até 200 KM e R$0,45 para viagens mais longas")
dist = int(input("Digite a distância da viagem: "))

if dist <= 200:
    preco = dist * 0.5
    print("O preço da passagem é de R${}{:.2f}{}".format('\033[1;33;45m',preco, '\033[m'))
else:
    preco2 = dist * 0.45
    print("O preço da passagem é de R${:.2f}".format(preco2))