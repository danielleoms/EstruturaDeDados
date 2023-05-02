# 13) Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas = []
soma_temperaturas = 0

# Recebe a temperatura média de cada mês e adiciona na lista de temperaturas
for i in range(12):
    temperatura = float(input(f"Digite a temperatura média de {meses[i]}: "))
    temperaturas.append(temperatura)
    soma_temperaturas += temperatura

# Calcula a média anual das temperaturas
media_anual = soma_temperaturas / 12

# Armazena os índices e valores das temperaturas acima da média anual em uma nova lista
acima_da_media = []
for i in range(12):
    if temperaturas[i] > media_anual:
        acima_da_media.append((i, temperaturas[i]))

# Imprime as temperaturas acima da média anual e o mês correspondente
print("Temperaturas acima da média anual:")
for i in range(len(acima_da_media)):
    mes = meses[acima_da_media[i][0]]
    temperatura = acima_da_media[i][1]
    print(f"{mes}: {temperatura:.2f}")
