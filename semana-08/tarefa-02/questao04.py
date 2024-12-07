altura = float(input("Digite sua altura: "))
sexo = int(input("Digite seu sexo [1] - Masculino [2] - Feminino: "))

if sexo == 1:
    pesoIdeal = (72.7 * altura) - 58
elif sexo == 2:
    pesoIdeal = (62.1 * altura) - 44.7

print(f"{pesoIdeal:.2f}")
