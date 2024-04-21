print("Olá, bem vindo ao banco VivuLichoPanu, sua solicitação de emprestimo será feita")
valorcasa = float(input("Gostaria de saber o valor da casa a ser comprada: "))
tempo = int(input("Gostaria também de saber em quantos anos gostaria de dividir as parcelas: "))
salario = float(input("Digite seu salário: "))

print("Vamor verificar se é possível realizar o empréstimo, se caso o valor da parcela for maior que 30% do seu salário, não será possível")

meses = tempo * 12
prestacao = valorcasa/meses
porcent = salario * 0.3

if prestacao < porcent:
    print("Parabéns, seu empréstimo será feito!")
elif prestacao > porcent:
    print("Seu salário não é suficiente para pagar as parcelas, logo o empréstimo não será feito")
