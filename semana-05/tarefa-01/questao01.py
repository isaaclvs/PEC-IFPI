def calcular(a, b, c):
    return 2 * a + 5 * b - c


primeiroNumero = int(input("Digite um numero: "))
segundoNumero = int(input("Digite um numero: "))
terceiroNumero = int(input("Digite um numero: "))

print(
    f"O resultado da expressao e: {calcular(primeiroNumero, segundoNumero, terceiroNumero)}"
)
