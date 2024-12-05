caractere = input("Digite algo: ")

VOGAIS = ["A", "E", "I", "O", "U"]

if caractere.isalnum():
    if caractere.isalpha():
        if caractere.upper() in VOGAIS:
            print("vogal")
        else:
            print("consoante")
    else:
        print("número")
else:
    print("símbolo")
