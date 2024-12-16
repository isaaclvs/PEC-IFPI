primeiroNumero = int(input("Digite o primeiro numero: "))
segundoNumero = int(input("Digite o segundo numero: "))
terceiroNumero = int(input("Digite o terceiro numero: "))

if primeiroNumero >= segundoNumero:
    diferencaSegundo = primeiroNumero - segundoNumero
else:
    diferencaSegundo = segundoNumero - primeiroNumero

if primeiroNumero >= terceiroNumero:
    diferencaTerceiro = primeiroNumero - terceiroNumero
else:
    diferencaTerceiro = terceiroNumero - primeiroNumero

if diferencaSegundo < diferencaTerceiro:
    print(diferencaSegundo)
elif diferencaTerceiro < diferencaSegundo:
    print(diferencaTerceiro)
else:
    print(diferencaSegundo)

