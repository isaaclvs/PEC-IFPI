numero = int(input("Digite um numero: "))

resto = numero % 5

if resto == 0:
    print((9 * numero) + 7)
elif resto == 1:
    if resto == 2:
        print("Par")
    else:
        print("ímpar")
elif resto == 2:
    print((5 * numero ** 2) - (3 * numero) + 42)
elif resto == 3:
    print(numero // 10)
elif resto == 4:
    print(numero ** 2)
