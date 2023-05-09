
#Escreva um Método em python para remover elementos repetidos de uma pilha#

class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        return self.itens.pop()

    def esta_vazia(self):
        return len(self.itens) == 0

    def remover_duplicatas(self):
        itens_vistos = set()
        resultado = []
        while not self.esta_vazia():
            item = self.desempilhar()
            if item not in itens_vistos:
                resultado.append(item)
                itens_vistos.add(item)
        resultado.reverse()
        self.itens = resultado


s = Pilha()
s.empilhar(3)
s.empilhar(3)
s.empilhar(3)
s.empilhar(6)
s.empilhar(6)
s.empilhar(9)
s.empilhar(10)
s.empilhar(12)

print("Pilha original:", s.itens)
s.remover_duplicatas()
print("Pilha sem duplicatas:", s.itens)

#Relatório#
"""
- O código foi reescrito utilizando uma estrutura de dados de pilha
- O método remover_duplicatas usa um conjunto (set) para rastrear quais itens já foram vistos anteriormente na pilha.
Em seguida, o método itera sobre cada item na pilha original e adiciona o item à pilha de resultado
somente se ele ainda não tiver sido visto.Por fim, a pilha de resultado é invertida para que os elementos 
apareçam na ordem correta e a pilha original é atualizada com os elementos não duplicados."""
