nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if nota3 > 8.0:
    media += 1
    if media > 10.0:
        media = 10.0

print(f"Media: {media}")
