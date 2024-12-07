matricula = input("Digite a matricula: ")
notas = []

notas.append(float(input("Digite a primeria nota: ")))
notas.append(float(input("Digite a segunda nota: ")))
notas.append(float(input("Digite a terceira nota: ")))

mediaExercicios = float(input("Digite a media dos exercicios: "))

mediaFinal = (notas[0] + (notas[1] * 2) + (notas[2] * 3) + mediaExercicios) / 7

if mediaFinal >= 9.0:
    conceito = "A"
elif (mediaFinal >= 7.5) and (mediaFinal < 9.0):
    conceito = "B"
elif (mediaFinal >= 6.0) and (mediaFinal < 7.5):
    conceito = "C"
elif (mediaFinal >= 4.0) and (mediaFinal < 6.0):
    conceito = "D"
elif mediaFinal < 4.0:
    conceito = "F"

print(matricula)
print(f"{mediaFinal:.2f}")
print(conceito)

if conceito in ["A", "B", "C"]:
    print("Aprovado")
else:
    print("Reprovado")
