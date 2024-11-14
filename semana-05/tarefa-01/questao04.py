minutos = int(input("Digite a quantidade de minutos: "))

horas = minutos // 60
minutosRestantes = minutos % 60

print(f"{horas}:{minutosRestantes}")
