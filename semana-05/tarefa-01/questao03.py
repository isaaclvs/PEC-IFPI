preco = float(input("Digite o preco: "))
percentual = (float(input("Digite o percentual: ")) / 100) * preco

valorAcrescimo = preco + percentual
valorDesconto = preco - percentual

print(f"Valor com valor com acrescimo: {valorAcrescimo:.2f}")
print(f"Valor com desconto: {valorDesconto:.2f}")
