tempoServico = int(input("Digite o tempo de serviço: "))
bonusAnoTrabalhado = float(input("Digite o valor do bonus por ano trabalhado: "))

bonificacao = tempoServico * bonusAnoTrabalhado

print(f"Essa é a bonificação: R${bonificacao:.2f}")
