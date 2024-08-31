import json

def carregar_dados (faturamento_aleatorio):
    with open(faturamento_aleatorio, 'r') as file:
        dados = json.load(file)
    return(dados)

def calcular_faturamento(dados):
    faturamento_valido = [dia['faturamento'] for dia in dados if dia ['faturamento'] > 0]
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    media_mensal = sum(faturamento_valido)/ len(faturamento_valido)
    dias_acima_da_media = sum(1 for dia in faturamento_valido if dia > media_mensal)
    return menor_faturamento, maior_faturamento, dias_acima_da_media

dados_faturamento = carregar_dados('faturamento_aleatorio.json')
menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_faturamento(dados_faturamento)

print(f"Menor faturamento do mês foi:R$ {menor_faturamento:.2f}")
print(f"Maior faturamento do mês foi:R$ {maior_faturamento:.2f}")
print(f"Total de dias com faturamento acima da média: {dias_acima_da_media}")