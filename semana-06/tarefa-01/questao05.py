valorCompra = float(input("Digite o valor da compra: "))

valorAvista = valorCompra - (9/100 * valorCompra)

valorPrestacao5x = valorCompra / 5

valorPrestacao10x = (valorCompra + (17/100 * valorCompra)) / 10

print(f"Valor a vista: {valorAvista:.2f}")
print(f"Valor em 5x: {valorPrestacao5x:.2f}")
print(f"Valor em 10x: {valorPrestacao10x:.2f}")
