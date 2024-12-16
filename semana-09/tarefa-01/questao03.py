base = int(input("Digite a base do poligono: "))
altura = int(input("Digite a altura: "))

if base == altura:
    print("QUADRADO")
else:
    perimetro = (2 * base) + (2  * altura)
    area = base * altura

    print(f"{perimetro} - {area}")
