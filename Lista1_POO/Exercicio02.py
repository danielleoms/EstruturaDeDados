# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def get_lado(self):  # get
        return self.lado

    def set_lado(self, lado):  # set
        self.lado = lado

    def area(self):
        return self.lado * self.lado
