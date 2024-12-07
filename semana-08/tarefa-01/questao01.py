diaAtual = int(input("Digite o Dia Atual: "))
mesAtual = int(input("Digite o Mes Atual: "))
anoAtual = int(input("Digite o Ano Atual: "))

diaNascimento = int(input("Digite o Dia do Nascimento: "))
mesNascimento = int(input("Digite o Mes do Nascimento: "))
anoNascimento = int(input("Digite o Ano do Nascimento: "))

idade = anoAtual - anoNascimento

if (mesAtual < mesNascimento) or (mesAtual == mesNascimento and diaAtual < diaNascimento):
    idade -= 1

print(f"Idade: {idade}")
