texto = input("Informe a palavra que deseja inverter: ")

texto_invertido = ""
for i in range(len(texto)-1, -1, -1):
    texto_invertido += texto[i]

print(f"A palavra escolhida fica dessa forma quando invertida: {texto_invertido}")