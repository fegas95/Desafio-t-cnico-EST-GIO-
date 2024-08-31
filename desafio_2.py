numero = int(input("informe um número para iniciar a verificação se o mesmo pertence a sequência fibonacci: "))
a, b = 0, 1

while b < numero:
    a, b = b, a + b

if b == numero or numero == 0:
    print(f"O número {numero} pertence a sequência de fibonacci.")
else:
    print(f"O número {numero} não pertence a sequência de fibonacci.")