#Danielle Moreno e Lucas Santini
# Escreva um método em python para remover elementos cujos valores estão em um range específico em uma lista encadeada

class Nodo:
    def __init__(self, dado=None, proximo=None):
        self.dado = dado
        self.proximo = proximo

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def __str__(self):
        resultado = ""
        nodo_atual = self.cabeca
        while nodo_atual:
            resultado += str(nodo_atual.dado) + " -> "
            nodo_atual = nodo_atual.proximo
        resultado += "None"
        return resultado

    def insere_no_inicio(self, valor):
        novo_nodo = Nodo(valor, self.cabeca)
        self.cabeca = novo_nodo

    def remove(self, valor):
        assert self.cabeca, "Não foi possivel remover valor de lista vazia."

        if self.cabeca.dado == valor:
            self.cabeca = self.cabeca.proximo
        else:
            anterior = None
            corrente = self.cabeca
            while corrente and corrente.dado != valor:
                anterior = corrente
                corrente = corrente.proximo
            if corrente:
                anterior.proximo = corrente.proximo
            else:
                anterior.proximo = None


lista = ListaEncadeada()
for i in range(15):
    lista.insere_no_inicio(i)
print("Lista:", lista)

print("====*===="*15)
print("                                                     Removendo elementos")
print("====*===="*15)
for i in range(15):
    lista.remove(i)
    print("Removendo o elemento {0}: {1}".format(i, lista))