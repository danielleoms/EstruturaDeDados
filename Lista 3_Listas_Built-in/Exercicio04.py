# 4) Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

import string

vogais = "aeiouAEIOU"
consoantes = ""
n_consoantes = 0

vetor = []
for i in range(10):
    while True:
        caractere = input(f"Digite o {i+1}º caractere: ")
        if len(caractere) == 1 and caractere not in string.punctuation and not caractere.isdigit():
            break
    vetor.append(caractere)

for caractere in vetor:
    if caractere not in vogais:
        n_consoantes += 1
        consoantes += caractere + " "

print(f"Consoantes lidas: {n_consoantes}\n{consoantes}")
