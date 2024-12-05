nome = input("Digite seu nome: ")
estadoCivil = int(input("Digite 1 para Casado e 2 para solteiro: "))

if estadoCivil == 1:
    nomeConjuge = input("Digite o nome do seu conjuge: ")
    totalCaracteres = (len(nome)) + (len(nomeConjuge))
else:
    totalCaracteres = len(nome)

print(totalCaracteres)
