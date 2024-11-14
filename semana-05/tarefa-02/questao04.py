caractere = input("Digite um caractere: ")

if caractere.isalnum():
    if caractere.isalpha() or int(caractere) in range(0, 10):
        print("True")
else:
    print("False")
