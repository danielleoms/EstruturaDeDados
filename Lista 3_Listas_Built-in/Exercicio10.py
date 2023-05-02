# 10) Faça um Programa que leia dois vetores com 10 elementos cada.
# Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

import random

vetor1 = [random.randrange(10) for i in range(10)]
vetor2 = [random.randrange(10) for i in range(10)]
vetor3 = []

for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print(f"O vetor 1 formado é: {vetor1}")
print(f"O vetor 2 formado é: {vetor2}")
print(f"O vetor 3 intercalado formado é: {vetor3}")
