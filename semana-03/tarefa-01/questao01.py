totalFatias = int(input("Digite a quantidade de fatias: "))
totalAmigos = int(input("Digite a quantidade de pessoas: "))

print(f"Essa é a quantidade de fatias para cada um: {totalFatias // totalAmigos}")
print(f"Essa é a quantidade de fatias que sobram: {totalFatias % totalAmigos}")
