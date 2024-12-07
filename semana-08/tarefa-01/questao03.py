numeros = []

numeros.append(int(input("Digite o primeiro numero :")))
numeros.append(int(input("Digite o segundo numero :")))
numeros.append(int(input("Digite o terceiro numero :")))
numeros.append(int(input("Digite o quarto numero :")))
numeros.append(int(input("Digite o quinto numero :")))

maiorNumero = numeros[0]
menorNumero = numeros[0]

for i in numeros:
    if i > maiorNumero:
        maiorNumero = i 
    if i < menorNumero:
        menorNumero = i 

print(f"Maior numero: {maiorNumero}")

print(f"Menor numero: {menorNumero}")
