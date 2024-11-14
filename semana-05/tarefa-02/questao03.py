caractere = input("Digite um caractere para saber se e consoante: ")

vogais = ["A", "E", "I", "O", "U"]

print("True") if caractere.isalpha() and caractere.upper() not in vogais else print(
    "False"
)
