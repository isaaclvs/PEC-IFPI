distanciaKm = int(input("Digite a distancia em Km: "))
velocidadeNave = int(input("Digite a velocidade da nave em Km/h"))

tempoHoras = distanciaKm // velocidadeNave
dias = tempoHoras // 24
horas = tempoHoras % 24

print(f"{dias} dias e {horas} horas")
