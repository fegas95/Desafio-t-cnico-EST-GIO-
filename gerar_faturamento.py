import json
import random

def gerar_dados_faturamento(nome_arquivo, numero_dias=30):
    dados = []
    for dia in range(1, numero_dias + 1):
        faturamento = round(random.uniform(0,2000),2)
        dados.append({"dia":dia,"faturamento":faturamento})

    with open(nome_arquivo, 'w') as file:
        json.dump(dados, file, indent=4)

gerar_dados_faturamento("faturamento_aleatorio.json")