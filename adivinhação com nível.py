#instruções
print('nível 1= 1 á 10')
print('nível 2= 1 á 50')
print('nível 3 1 á 100')
#dificuldade
nivel = int(input("escolha o nível: nivel 1, 2 ou 3 "))
max_numero = 10 if nivel == 1 else 50 if nivel == 2 else 100
#base do projeto
n=0
while n > 9:
    n=[0,1,2,3,4,5,6,7,8,9]
escolha=int(input('um número; '))
if escolha==n:
    print('acertou!')
elif escolha!=n:
    print('tente novamente')
print(n)
tentativas = 10 if nivel == 1 else 5 if nivel == 2 else 3