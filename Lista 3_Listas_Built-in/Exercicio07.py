# 7) Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetor = []
soma = 0
produto = 1

for i in range(5):
    numero = int(input(f"Informe o {i + 1}º número: "))
    vetor.append(numero)
    soma += numero
    produto *= numero

print("Números informados:", vetor)
print("Soma:", soma)
print("Multiplicação:", produto)
