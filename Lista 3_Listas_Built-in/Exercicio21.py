""" 21) Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
 Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um
 litro de combustível. Calcule e mostre:
a - O modelo do carro mais econômico;
b - Quantos litros de combustível cada um dos carros cadastrados consome para percorrer
uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.
Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo.
Os dados são fictícios e podem mudar a cada execução do programa."""

def calcular_litros(distancia, consumo):
    return distancia / consumo

modelos = []
consumo = []
litros = []

print("Comparativo de Consumo de Combustível")

for i in range(1, 6):
    print(f"Veículo {i}")
    modelos.append(str(input("Nome: ")))
    while True:
        consumo_carro = float(input("Km por litro: "))
        if consumo_carro > 0:
            break
        print("Valor inválido. Por favor, informe um valor maior que zero.")
    consumo.append(consumo_carro)

print("\nRelatório final:")

print(f"{'Nº':<2} - {'Modelo':<10} - {'Km/L':>5} - {'Litros (1000 km)':>15} - {'Custo (1000 km)':>15}")
cont = 1

for m, c in zip(modelos, consumo):
    litros_carro = calcular_litros(1000, c)
    print(f"{cont:<2} - {m:<10} - {c:>5} - {litros_carro:>15.2f} - R${litros_carro * 2.25:>14.2f}")
    cont += 1

indice_menor_consumo = consumo.index(min(consumo))
print(f"\nO menor consumo é do {modelos[indice_menor_consumo]}") 
