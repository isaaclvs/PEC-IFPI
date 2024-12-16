primeiroNumero = int(input("Primeiro valor: "))
segundoNumero = int(input("Segundo valor: "))
terceiroNumero = int(input("Terceiro valor: "))


if (primeiroNumero == segundoNumero) and (primeiroNumero == terceiroNumero):
    print("Todos os valores são iguais") 
elif (primeiroNumero != segundoNumero) and (primeiroNumero != terceiroNumero) and (segundoNumero != terceiroNumero):
    print("Todos os valores são diferentes")
else:
    print("Existem dois valores iguais e um diferente")
