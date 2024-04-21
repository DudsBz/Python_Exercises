nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:@^10}!'.format(nome))

n1 = float (input('Digite um valor : '))
n2 = int (input('Digite outro : '))
s = n1+n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print ('A soma é {}, o produto é {}, a divisão é {}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a potência é {}'.format(di, e))
