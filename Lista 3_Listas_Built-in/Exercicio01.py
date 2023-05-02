# 1) Faça um Programa que leia um vetor de 5 números inteiros e mostre-os

import random

# cria uma lista vazia
lista = []

# itera 5 vezes, adicionando um número inteiro aleatório (entre 0 e 9) à lista a cada iteração
for i in range(5):
    lista.append(random.randrange(10))

# imprime a lista na tela, separando cada número por um espaço em branco
print("A lista é: ", end="")
for e in lista:
    print(e, end=" ")
