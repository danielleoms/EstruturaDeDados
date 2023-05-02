# Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;


class Retangulo:
    def __init__(self, comp, largura):
        self.comp = comp
        self.largura = largura

    def mostra_comp(self):  # get
        return self.comp

    def troca_comp(self, valor):  # set
        self.comp = valor

    def mostra_largura(self):  # get
        return self.largura

    def troca_largura(self, valor):  # set
        self.largura = valor

    def area(self):
        return self.largura * self.comp

    def perimetro(self):
        return 2 * (self.largura + self.comp)


if __name__ == "__main__":
    comp = float(input("Informe o comprimento do local (em m): "))
    largura = float(input("Informe a largura do local (em m): "))
    local = Retangulo(comp, largura)
    print(f"A area do local é {local.area()}m² e o perimetro do local é {local.perimetro()}m")
