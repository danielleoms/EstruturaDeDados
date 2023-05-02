# Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho
# (estomago) e pelo menos os métodos comer(), verBucho() e digerir().
# Faça um programa ou teste interativamente, criando pelo menos dois macacos,
# alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do
# estomago a cada refeição. Experimente fazer com que um macaco coma o outro.
# É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome, estomago=[]):
        self.nome = nome
        self.estomago = estomago

    def comer(self, comida):
        self.estomago.append(comida)

    def ver_bucho(self):
        return self.estomago

    def digerir(self, comida):
        self.estomago.remove(comida)


macaco1 = Macaco('Chico')
macaco1.comer("banana")
print(macaco1.ver_bucho())
macaco1.comer("ração")
print(macaco1.ver_bucho())
macaco1.digerir("ração")
print(macaco1.ver_bucho())
macaco1.comer("melancia")
print(macaco1.ver_bucho())
macaco1.digerir("melancia")
print(macaco1.ver_bucho())

macaco2 = Macaco('Sabrina', ['kiwi'])
print(macaco2.ver_bucho())
macaco2.comer(macaco1)
print(macaco2.ver_bucho())
macaco2.digerir(macaco1)
print(macaco2.ver_bucho())
macaco2.comer("Melancia")
print(macaco2.ver_bucho())
