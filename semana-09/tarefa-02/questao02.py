# Função para converter números para texto
def numero_por_extenso(n):
    numeros = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    return numeros[n]

numero = int(input())

if numero < 0 or numero >= 1000:
    print("O número deve ser menor que 1000.")
else:
    # Separação de centenas, dezenas e unidades
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    partes = []

    # Centenas
    if centenas > 0:
        texto_centenas = f"{numero_por_extenso(centenas)} {'centena' if centenas == 1 else 'centenas'}"
        partes.append(texto_centenas)

    # Dezenas
    if dezenas > 0:
        texto_dezenas = f"{numero_por_extenso(dezenas)} {'dezena' if dezenas == 1 else 'dezenas'}"
        partes.append(texto_dezenas)

    # Unidades
    if unidades > 0:
        texto_unidades = f"{numero_por_extenso(unidades)} {'unidade' if unidades == 1 else 'unidades'}"
        partes.append(texto_unidades)

    # Formatação
    if len(partes) == 1:
        resultado = partes[0]
    elif len(partes) == 2:
        resultado = partes[0] + " e " + partes[1]
    else:
        resultado = partes[0] + ", " + partes[1] + " e " + partes[2]

    print(f"{resultado}.")

