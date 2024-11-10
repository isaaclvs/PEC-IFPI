alturaMetros = float(input("Digite a altura da sala em Metros: "))
comprimentoMetros = float(input("Digite o comprimento da sala em Metros: "))
larguraMetros = float(input("Digite a largura da sala em Metros: "))

areaPiso = larguraMetros * comprimentoMetros
volumeSala = larguraMetros * comprimentoMetros * alturaMetros
areaParedes = 2 * alturaMetros * larguraMetros + 2 * alturaMetros * comprimentoMetros

print(f"A area do piso: {areaPiso}")
print(f"O volume da sala: {volumeSala}")
print(f"A area das paredes: {areaParedes}")
