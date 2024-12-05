nome = input("Digite seu nome: ")
sexo = int(input("Digite [1] para Homem e [2] para mulher: "))

if sexo == 1:
    print(f"Ilmo Sr. {nome}")
elif sexo == 2:
    print(f"Ilma Sra. {nome}")

