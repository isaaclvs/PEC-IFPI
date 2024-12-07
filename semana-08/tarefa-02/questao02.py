numero = int(input("Digite um numero: "))
soma = 0

if numero in range(0, 100000):
    for i in str(numero):
        soma += int(i) 
    print(soma)
else:
    print("-1")
