numeros = []

numeros.append(float(input("Digite o primeiro numero: ")))
numeros.append(float(input("Digite o segundo numero: ")))
numeros.append(float(input("Digite o terceiro numero: ")))
numeros.append(float(input("Digite o quarto numero: ")))
numeros.append(float(input("Digite o quinto numero: ")))

media = 0

for i in numeros:
    media += i 

media = media / 5.0

maiores = []

for i in numeros:
    if i > media:
        maiores.append(i)

print(f"Media: {media:.2f}")

for i in maiores:
    print(i)
