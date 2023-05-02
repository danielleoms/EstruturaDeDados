# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor .
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para
# gerar numeros aleatórios, simulando os lançamentos dos dados.

import random

resultados = [0] * 6 # cria uma lista com 6 elementos iniciados com valor 0

for i in range(100):
    lancamento = random.randint(1, 6) # gera um número aleatório entre 1 e 6
    resultados[lancamento - 1] += 1 # incrementa o contador do valor obtido no lançamento

# imprime o número de vezes que cada valor foi conseguido
for i in range(6):
    print(f"O valor {i+1} foi obtido {resultados[i]} vezes.")
