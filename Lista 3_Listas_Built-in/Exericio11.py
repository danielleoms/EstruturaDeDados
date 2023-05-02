# 11) Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

import random

vetor1 = [random.randrange(10) for _ in range(10)]
vetor2 = [random.randrange(10) for _ in range(10)]
vetor3 = [random.randrange(10) for _ in range(10)]

vetor_intercalado = []

for i in range(10):
    vetor_intercalado.append(vetor1[i])
    vetor_intercalado.append(vetor2[i])
    vetor_intercalado.append(vetor3[i])

print(f"Vetor 1: {vetor1}")
print(f"Vetor 2: {vetor2}")
print(f"Vetor 3: {vetor3}")
print(f"Vetor intercalado: {vetor_intercalado}")
