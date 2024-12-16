x = int(input("Primeiro numero: "))
y = int(input("Segundo Numero: "))

operacao = int(input("[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão\n"))

if operacao == 1:
    print(x + y)
elif operacao == 2:
    print(x - y)
elif operacao == 3:
    print(x * y)
elif operacao == 4:
    print(x / y)
