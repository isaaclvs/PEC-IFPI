respostas_positivas = 0

resposta1 = input().strip().upper()
if resposta1 == "S":
    respostas_positivas += 1

resposta2 = input().strip().upper()
if resposta2 == "S":
    respostas_positivas += 1

resposta3 = input().strip().upper()
if resposta3 == "S":
    respostas_positivas += 1

resposta4 = input().strip().upper()
if resposta4 == "S":
    respostas_positivas += 1

resposta5 = input().strip().upper()
if resposta5 == "S":
    respostas_positivas += 1

if respostas_positivas == 2:
    classificacao = "Suspeito"
elif respostas_positivas in [3, 4]:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print(classificacao)

