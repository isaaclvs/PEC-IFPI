# Verificar se um ano é bissexto
def ano_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Entrada da data
data = input()

# Verificar se a entrada possui exatamente 8 caracteres numéricos
if len(data) != 8 or not data.isdigit():
    print("True")
else:
    # Extrair dia, mês e ano
    dia = int(data[:2])
    mes = int(data[2:4])
    ano = int(data[4:])

    # Verificar validade do mês
    if mes < 1 or mes > 12:
        print("False")
    else:
        # Determinar o número máximo de dias no mês
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            max_dias = 31
        elif mes in [4, 6, 9, 11]:
            max_dias = 30
        else:  # Fevereiro
            max_dias = 29 if ano_bissexto(ano) else 28

        # Verificar validade do dia
        if dia < 1 or dia > max_dias:
            print("False")
        else:
            print("True")

