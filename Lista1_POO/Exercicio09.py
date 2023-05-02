# Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

# Possua uma classe chamada Ponto, com os atributos x e y.
# Possua uma classe chamada Retangulo, com os atributos largura e altura.
# Possua uma função para imprimir os valores da classe Ponto
# Possua uma função para encontrar o centro de um Retângulo.
# Você deve criar alguns objetos da classe Retangulo.
# Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo,
#   que deve ser um objeto da classe Ponto.
# A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto
#   que indique os valores de x e y para o centro do objeto.
# O valor do centro do objeto deve ser mostrado na tela
#  Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def retornar_x(self):
        return self.x

    def retornar_y(self):
        return self.y


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def centro_x(self):
        x = self.largura / 2
        return x

    def centro_y(self):
        y = self.altura / 2
        return y


while True:
    larg = float(input("Insira o largura do retâgulo:"))
    alt = float(input("Insira a altura do retângulo:"))
    retangulo1 = Retangulo(larg, alt)
    centro_ret01 = Ponto(retangulo1.centro_x(), retangulo1.centro_y())
    print(f"O centro do retângulo é ({centro_ret01.retornar_x()},{centro_ret01.retornar_y()})")
    resp = str(input("Deseja inserir os valores de mais um retâgulo [S/N] : ")).upper().strip()
    if resp == "N":
        break
