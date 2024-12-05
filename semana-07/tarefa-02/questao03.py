numero = int(input("Digite um numero entre 10 e 99: "))
digitos = 0

for i in str(numero):
    if int(i) % 2 != 0:
        digitos += 1

if digitos == 0:
    print("Nenhum dígito é ímpar.")
elif digitos == 1:
    print("Apenas um dígito é ímpar.")
elif digitos == 2:
    print("Os dois dígitos são ímpares.")
