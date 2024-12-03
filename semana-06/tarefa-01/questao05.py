valorCompra = float(input())

valorAvista = valorCompra - (9/100 * valorCompra)

valorPrestacao5x = valorCompra / 5

valorPrestacao10x = (valorCompra + (17/100 * valorCompra)) / 10

print(f"{valorAvista:.2f}")
print(f"{valorPrestacao5x:.2f}")
print(f"{valorPrestacao10x:.2f}")
