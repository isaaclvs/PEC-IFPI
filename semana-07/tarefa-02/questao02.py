numero = int(input("Digite um numero entre 100 e 999: "))
digitos = 0

for i in str(numero):
    if int(i) % 2 == 0:
        digitos += 1

print(digitos)
