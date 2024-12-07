numero = int(input("Digite um numero: "))

if (numero % 3 == 0) and (numero % 5 == 0):
    print("FIZZBUZZ")
elif numero % 3 == 0:
    print("FIZZ")
elif numero % 5 == 0:
    print("BUZZ")
else:
    print(numero)

