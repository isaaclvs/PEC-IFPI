pesoKg = float(input("Digite seu peso em Kg: "))
alturaCm = float(input("Digite sua altura em Cm: "))

imc = pesoKg / (alturaCm ** 2)

if imc < 18.5:
    print(f"{imc:2.2f}")
    print("Abaixo do peso")
elif imc < 25.0:
    print(f"{imc:2.2f}")
    print("Peso normal")
elif imc < 30.0:
    print(f"{imc:2.2f}")
    print("Sobrepeso")
elif imc < 35.0:
    print(f"{imc:2.2f}")
    print("Obeso leve")
elif imc < 40.0:
    print(f"{imc:2.2f}")
    print("Obeso moderado")
elif imc >= 40.0:
    print(f"{imc:2.2f}")
    print("Obeso mórbido")
