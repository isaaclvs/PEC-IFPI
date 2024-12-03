numeros = []

while len(numeros) < 5:
    numeros.append(int(input(f"Digite o numero: ")))

numeros.sort()

maior = numeros[len(numeros)-1]
menor = numeros[0]
mediaAritmetica = sum(numeros) / len(numeros)

print(f"Maior numero: {maior}")
print(f"Menor numero: {menor}")
print(f"Media Aritmetica: {mediaAritmetica}")
