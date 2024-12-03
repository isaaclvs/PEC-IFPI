tempoSegundos = int(input("Digite a quantidade de segundos: "))

horas = (tempoSegundos // 60) // 60

minutos = (tempoSegundos // 60) % 60

segundos = tempoSegundos % 60

print(f"{horas}:{minutos}:{segundos}")
