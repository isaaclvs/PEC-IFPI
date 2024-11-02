valorProduto = float(input("Digite o valor do produto: "))

valorComDesconto = valorProduto - (valorProduto * (10 / 100))

print(f"Com desconto de 10% o novo valor é: R${valorComDesconto:.2f}")
