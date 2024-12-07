primeiraData = []
primeiraData.append(int(input("Digite o Dia da Primeira data: "))) # Dia
primeiraData.append(int(input("Digite o Mes da Primeira data: "))) # Mes
primeiraData.append(int(input("Digite o Ano da Primeira data: "))) # Ano

segundaData = []
segundaData.append(int(input("Digite o Dia da Segunda data: "))) # Dia
segundaData.append(int(input("Digite o Mes da Segunda data: "))) # Mes
segundaData.append(int(input("Digite o Ano da Segunda data: "))) # Ano

if primeiraData[2] == segundaData[2]:
    if primeiraData[1] == segundaData[1]:
        if primeiraData[0] > segundaData[0]:
            maisRecente = primeiraData
        else:
            maisRecente = segundaData
    elif primeiraData[1] > segundaData[1]:
        maisRecente = primeiraData
    else:
        maisRecente = segundaData
elif primeiraData[2] > segundaData[2]:
    maisRecente = primeiraData
else:
    maisRecente = segundaData

print(f"{maisRecente[0]}/{maisRecente[1]}/{maisRecente[2]}")
